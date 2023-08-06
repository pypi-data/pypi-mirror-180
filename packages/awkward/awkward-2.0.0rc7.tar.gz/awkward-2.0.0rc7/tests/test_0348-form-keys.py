# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE

import pickle

import numpy as np
import pytest  # noqa: F401

import awkward as ak

ak_Array = ak.highlevel.Array
ak_Record = ak.highlevel.Record
ak_to_buffers = ak.operations.to_buffers
ak_from_buffers = ak.operations.from_buffers


def test_numpyarray():
    assert ak_from_buffers(*ak_to_buffers(ak_Array([1, 2, 3, 4, 5]))).tolist() == [
        1,
        2,
        3,
        4,
        5,
    ]
    assert pickle.loads(pickle.dumps(ak_Array([1, 2, 3, 4, 5]), -1)).tolist() == [
        1,
        2,
        3,
        4,
        5,
    ]


def test_listoffsetarray():
    assert ak_from_buffers(*ak_to_buffers([[1, 2, 3], [], [4, 5]])).tolist() == [
        [1, 2, 3],
        [],
        [4, 5],
    ]
    assert ak_from_buffers(
        *ak_to_buffers(["one", "two", "three", "four", "five"])
    ).tolist() == ["one", "two", "three", "four", "five"]
    assert ak_from_buffers(
        *ak_to_buffers([["one", "two", "three"], [], ["four", "five"]])
    ).tolist() == [["one", "two", "three"], [], ["four", "five"]]
    assert pickle.loads(
        pickle.dumps(ak_Array([[1, 2, 3], [], [4, 5]]), -1)
    ).tolist() == [[1, 2, 3], [], [4, 5]]


def test_listarray():
    listoffsetarray = ak_Array([[1, 2, 3], [], [4, 5]]).layout
    listarray = ak.contents.ListArray(
        listoffsetarray.starts, listoffsetarray.stops, listoffsetarray.content
    )
    assert ak_from_buffers(*ak_to_buffers(listarray)).tolist() == [
        [1, 2, 3],
        [],
        [4, 5],
    ]
    assert pickle.loads(pickle.dumps(ak_Array(listarray), -1)).tolist() == [
        [1, 2, 3],
        [],
        [4, 5],
    ]


def test_indexedoptionarray():
    assert ak_from_buffers(*ak_to_buffers([1, 2, 3, None, None, 5])).tolist() == [
        1,
        2,
        3,
        None,
        None,
        5,
    ]
    assert pickle.loads(
        pickle.dumps(ak_Array([1, 2, 3, None, None, 5]), -1)
    ).tolist() == [1, 2, 3, None, None, 5]


def test_indexedarray():
    content = ak_Array([0.0, 1.1, 2.2, 3.3, 4.4]).layout
    index = ak.index.Index64(np.array([3, 1, 1, 4, 2], dtype=np.int64))
    indexedarray = ak.contents.IndexedArray(index, content)
    assert ak_from_buffers(*ak_to_buffers(indexedarray)).tolist() == [
        3.3,
        1.1,
        1.1,
        4.4,
        2.2,
    ]
    assert pickle.loads(pickle.dumps(ak_Array(indexedarray), -1)).tolist() == [
        3.3,
        1.1,
        1.1,
        4.4,
        2.2,
    ]


def test_emptyarray():
    assert ak_from_buffers(*ak_to_buffers([])).tolist() == []
    assert ak_from_buffers(*ak_to_buffers([[], [], []])).tolist() == [[], [], []]

    assert pickle.loads(pickle.dumps(ak_Array([]), -1)).tolist() == []
    assert pickle.loads(pickle.dumps(ak_Array([[], [], []]), -1)).tolist() == [
        [],
        [],
        [],
    ]


def test_bytemaskedarray():
    content = ak_Array([0.0, 1.1, 2.2, 3.3, 4.4]).layout
    mask = ak.index.Index8(np.array([False, True, True, False, False], dtype=np.int8))
    bytemaskedarray = ak.contents.ByteMaskedArray(mask, content, True)
    assert ak_from_buffers(*ak_to_buffers(bytemaskedarray)).tolist() == [
        None,
        1.1,
        2.2,
        None,
        None,
    ]
    assert pickle.loads(pickle.dumps(ak_Array(bytemaskedarray), -1)).tolist() == [
        None,
        1.1,
        2.2,
        None,
        None,
    ]


def test_bitmaskedarray():
    content = ak_Array([0.0, 1.1, 2.2, 3.3, 4.4]).layout
    mask = ak.index.IndexU8(
        np.packbits(np.array([False, True, True, False, False], dtype=np.int8))
    )
    bitmaskedarray = ak.contents.BitMaskedArray(mask, content, True, 5, False)
    assert ak_from_buffers(*ak_to_buffers(bitmaskedarray)).tolist() == [
        None,
        1.1,
        2.2,
        None,
        None,
    ]
    assert pickle.loads(pickle.dumps(ak_Array(bitmaskedarray), -1)).tolist() == [
        None,
        1.1,
        2.2,
        None,
        None,
    ]


def test_recordarray():
    assert ak_from_buffers(
        *ak_to_buffers([(1.1, [1]), (2.2, [1, 2]), (3.3, [1, 2, 3])])
    ).tolist() == [(1.1, [1]), (2.2, [1, 2]), (3.3, [1, 2, 3])]
    assert ak_from_buffers(
        *ak_to_buffers(
            [{"x": 1.1, "y": [1]}, {"x": 2.2, "y": [1, 2]}, {"x": 3.3, "y": [1, 2, 3]}]
        )
    ).tolist() == [
        {"x": 1.1, "y": [1]},
        {"x": 2.2, "y": [1, 2]},
        {"x": 3.3, "y": [1, 2, 3]},
    ]

    assert pickle.loads(
        pickle.dumps(ak_Array([(1.1, [1]), (2.2, [1, 2]), (3.3, [1, 2, 3])]), -1)
    ).tolist() == [(1.1, [1]), (2.2, [1, 2]), (3.3, [1, 2, 3])]
    assert pickle.loads(
        pickle.dumps(
            ak_Array(
                [
                    {"x": 1.1, "y": [1]},
                    {"x": 2.2, "y": [1, 2]},
                    {"x": 3.3, "y": [1, 2, 3]},
                ]
            ),
            -1,
        )
    ).tolist() == [
        {"x": 1.1, "y": [1]},
        {"x": 2.2, "y": [1, 2]},
        {"x": 3.3, "y": [1, 2, 3]},
    ]


def test_record():
    assert pickle.loads(
        pickle.dumps(ak_Record({"x": 2.2, "y": [1, 2]}), -1)
    ).tolist() == {"x": 2.2, "y": [1, 2]}
    assert pickle.loads(
        pickle.dumps(
            ak_Array(
                [
                    {"x": 1.1, "y": [1]},
                    {"x": 2.2, "y": [1, 2]},
                    {"x": 3.3, "y": [1, 2, 3]},
                ]
            )[1],
            -1,
        )
    ).tolist() == {"x": 2.2, "y": [1, 2]}


def test_regulararray():
    content = ak_Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).layout
    regulararray = ak.contents.RegularArray(content, 3, zeros_length=0)
    assert ak_from_buffers(*ak_to_buffers(regulararray)).tolist() == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
    ]
    assert pickle.loads(pickle.dumps(ak_Array(regulararray), -1)).tolist() == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
    ]


def test_unionarray():
    assert ak_from_buffers(*ak_to_buffers([[1, 2, 3], [], 4, 5])).tolist() == [
        [1, 2, 3],
        [],
        4,
        5,
    ]
    assert pickle.loads(pickle.dumps(ak_Array([[1, 2, 3], [], 4, 5]), -1)).tolist() == [
        [1, 2, 3],
        [],
        4,
        5,
    ]


def test_unmaskedarray():
    content = ak_Array([1, 2, 3, 4, 5]).layout
    unmaskedarray = ak.contents.UnmaskedArray(content)
    assert ak_from_buffers(*ak_to_buffers(unmaskedarray)).tolist() == [1, 2, 3, 4, 5]
    assert pickle.loads(pickle.dumps(ak_Array(unmaskedarray), -1)).tolist() == [
        1,
        2,
        3,
        4,
        5,
    ]
