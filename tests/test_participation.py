import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pyParticipation.participation import (
    count_participants,
    count_measurements,
    measurements_per_participant,
    participant_measurement_summary,
    measurements_per_wave
)

### test_count_participants

def test_count_participants():
    df = pd.DataFrame({
        'participant_id': [1, 2, 2, 3]
    })
    assert count_participants(df, 'participant_id') == 3


### test_count_measurements

def test_count_measurements():
    df = pd.DataFrame({
        'participant_id': [1, 2, 3],
        'measurement': [10.1, None, 12.4]
    })
    assert count_measurements(df, 'measurement') == 2


### test_measurements_per_participant

def test_measurements_per_participant():
    df = pd.DataFrame({
        'participant_id': [1, 2, 2, 3, 3, 3],
        'measurement': [None, None, None, None, 4.1, 4.5]
    })
    result = measurements_per_participant(df, 'participant_id', 'measurement')
    expected = pd.DataFrame({
        'participant_id': [1, 2, 3],
        'measurement_count': [0, 0, 2]
    })
    pd.testing.assert_frame_equal(result.sort_values('participant_id').reset_index(drop=True), expected)


### test_participant_measurement_summary

def test_participant_measurement_summary():
    df = pd.DataFrame({
        'participant_id': [1, 2, 2, 3, 3, 3],
        'measurement': [None, None, None, None, 4.1, 4.5]
    })
    summary = participant_measurement_summary(df, 'participant_id', 'measurement')
    
    assert summary['count'] == 3
    assert summary['min'] == 0
    assert summary['max'] == 2
    assert summary['mean'] == (0 + 0 + 2) / 3


### test_measurements_per_wave_with_unscheduled

def test_measurements_per_wave_with_unscheduled():
    df = pd.DataFrame({
        'wave': [1, 1, 2, 2, 3, 3, None],
        'measurement': [None, 98.6, 99.1, None, None, None, 100.2]
    })
    result = measurements_per_wave(df, 'wave', 'measurement', include_unscheduled=True)
    expected = pd.Series([1, 1, 0, 1], index=['1', '2', '3', 'UNSCHEDULED/UNKNOWN'], dtype='int64')
    pd.testing.assert_series_equal(result.sort_index(), expected.sort_index())
