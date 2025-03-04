# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

import unittest
from unittest.mock import MagicMock, patch

from paths.build_output_dir import BuildOutputDir


class BuildOutputDirTests(unittest.TestCase):

    @patch("paths.output_dir.os")
    def test(self, mock_os):

        mock_cwd = MagicMock()
        mock_os.getcwd.return_value = mock_cwd

        mock_dir = MagicMock()
        mock_os.path.join.return_value = mock_dir

        BuildOutputDir("opensearch", makedirs=True)

        mock_os.path.join.assert_called_once_with(
            mock_cwd,
            "builds",
            "opensearch"
        )

        mock_os.makedirs.assert_called_once_with(mock_dir, exist_ok=True)

    @patch("paths.output_dir.os")
    def test_opensearch_dashboards(self, mock_os):

        mock_cwd = MagicMock()
        mock_os.getcwd.return_value = mock_cwd

        mock_dir = MagicMock()
        mock_os.path.join.return_value = mock_dir

        BuildOutputDir("opensearch-dashboards", makedirs=True)

        mock_os.path.join.assert_called_once_with(
            mock_cwd,
            "builds",
            "opensearch-dashboards"
        )

        mock_os.makedirs.assert_called_once_with(mock_dir, exist_ok=True)

    @patch("paths.output_dir.os")
    def test_with_cwd(self, mock_os):
        mock_dir = MagicMock()
        mock_os.path.join.return_value = mock_dir

        BuildOutputDir("opensearch", cwd="test_cwd", makedirs=False)

        mock_os.path.join.assert_called_once_with(
            "test_cwd",
            "builds",
            "opensearch"
        )

        mock_os.makedirs.assert_not_called()
        mock_os.getcwd.assert_not_called()
