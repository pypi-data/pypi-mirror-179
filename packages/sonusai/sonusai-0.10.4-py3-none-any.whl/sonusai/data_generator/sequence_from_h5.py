import warnings

import numpy as np

with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    from keras.utils import Sequence


class SequenceFromH5(Sequence):
    """Generates data from a directory containing genft data"""
    from dataclasses import dataclass
    from typing import List

    @dataclass(frozen=True)
    class BatchParams:
        from typing import List

        idx: List[int]
        offset: int
        extra: int

    def __init__(self,
                 files: List[str],
                 feature: str,
                 num_classes: int,
                 batch_size: int,
                 timesteps: int,
                 flatten: bool,
                 add1ch: bool,
                 truth_mutex: bool):
        """Initialization"""
        from os.path import exists

        import h5py

        from sonusai import SonusAIError
        from sonusai.data_generator import get_frames_per_batch

        self.files = files
        self.feature = feature
        self.num_classes = num_classes
        self.batch_size = batch_size
        self.timesteps = timesteps
        self.flatten = flatten
        self.add1ch = add1ch
        self.truth_mutex = truth_mutex

        for file in self.files:
            if not exists(file):
                raise SonusAIError(f'Could not find {file}')
            with h5py.File(file, 'r') as f:
                if 'feature' not in f:
                    raise SonusAIError(f'Could not find "feature" in {file}')

        self.stride = self.mixdb.fg.stride
        self.num_bands = self.mixdb.fg.num_bands
        self.frames_per_batch = get_frames_per_batch(self.batch_size, self.timesteps)

        # Compute idx, offset, and extra for dataset
        # offsets and extras are needed because files are not guaranteed to fall on batch boundaries.
        # When fetching a new index that starts in the middle of a sequence of files, the
        # previous feature frame offset must be maintained in order to preserve the correct
        # data sequence. And the extra must be maintained in order to preserve the correct data length.
        cumulative_frames = 0
        start_file_index = 0
        offset = 0
        self.batch_params = []
        self.file_indices = []
        total_frames = 0
        for i in range(len(self.files)):
            current_frames = self._get_feature(i).shape[0]
            self.file_indices.append(slice(total_frames, total_frames + current_frames))
            total_frames += current_frames
            cumulative_frames += current_frames
            while cumulative_frames >= self.frames_per_batch:
                extra_frames = cumulative_frames - self.frames_per_batch
                idx = list(range(start_file_index, i + 1))
                self.batch_params.append(self.BatchParams(idx=idx, offset=offset, extra=extra_frames))
                if extra_frames == 0:
                    start_file_index = i + 1
                    offset = 0
                else:
                    start_file_index = i
                    offset = current_frames - extra_frames
                cumulative_frames = extra_frames

        if cumulative_frames > 0:
            extra_frames = cumulative_frames - self.frames_per_batch
            idx = list(range(start_file_index, len(self.files)))
            self.batch_params.append(self.BatchParams(idx=idx, offset=offset, extra=extra_frames))

        self.total_batches = int(np.ceil(total_frames / self.frames_per_batch))

    def __len__(self) -> int:
        """Denotes the number of batches per epoch"""
        return self.total_batches

    def __getitem__(self, batch_index: int) -> np.ndarray:
        """Get one batch of data"""
        from sonusai.utils import reshape_inputs

        batch_params = self.batch_params[batch_index]

        result = []
        for idx in batch_params.idx:
            result.append(self._get_feature(idx))

        feature = np.vstack([result[i] for i in range(len(result))])

        if batch_params.extra > 0:
            feature = feature[batch_params.offset:-batch_params.extra]
        else:
            feature = feature[batch_params.offset:]
            if batch_params.extra < 0:
                feature = np.pad(array=feature, pad_width=((0, -batch_params.extra), (0, 0), (0, 0)))

        feature, _ = reshape_inputs(feature=feature,
                                    batch_size=self.batch_size,
                                    timesteps=self.timesteps,
                                    flatten=self.flatten,
                                    add1ch=self.add1ch)

        return feature

    def _get_feature(self, idx: int) -> np.ndarray:
        import h5py

        with h5py.File(self.files[idx], 'r') as f:
            return np.array(f['feature'])
