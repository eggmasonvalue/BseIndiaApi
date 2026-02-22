import unittest
from unittest.mock import MagicMock, patch
from pathlib import Path
from context import BSE

class TestBSE(unittest.TestCase):
    def setUp(self):
        self.bse = BSE(download_folder=Path("."))

    @patch("bse.BSE.Session")
    def test_getScripGroups(self, mock_session):
        # Setup mock response
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {"Symbol": "A"},
            {"Symbol": "B"},
            {"Symbol": "C"}
        ]
        mock_response.ok = True

        # Inject mock session into BSE instance
        self.bse.session = MagicMock()
        self.bse.session.get.return_value = mock_response

        # Call the method
        groups = self.bse.getScripGroups()

        # Verify assertions
        self.assertEqual(groups, ["A", "B", "C"])
        self.bse.session.get.assert_called_with(
            "https://api.bseindia.com/BseIndiaAPI/api/BindDDLEQ/w",
            params={"flag": "Group"},
            timeout=10
        )

if __name__ == "__main__":
    unittest.main()
