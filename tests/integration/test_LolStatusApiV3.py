import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


@pytest.mark.integration
@pytest.mark.parametrize(
    "region",
    [
        "br1",
        "eun1",
        "euw1",
        "jp1",
        "kr",
        "la1",
        "la2",
        "na",
        "na1",
        "oc1",
        "tr1",
        "ru",
        "pbe1",
    ],
)
class TestStatusApiV3(object):
    def test_shard_data(self, mock_context, region):
        actual_response = mock_context.watcher.lol_status.shard_data(region)

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/status/v3/shard-data".format(
                region=region
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )
