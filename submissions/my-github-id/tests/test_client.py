from unittest.mock import Mock, patch
from banking_client.client import BankingClient
from banking_client.models import TransferResponse


@patch('requests.Session.post')
def test_transfer_success(mock_post):
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "transactionId": "tx-123",
        "status": "SUCCESS",
        "message": "OK",
        "fromAccount": "ACC1000",
        "toAccount": "ACC1001",
        "amount": 100.0,
    }
    mock_post.return_value = mock_resp

    client = BankingClient()
    result = client.transfer("ACC1000", "ACC1001", 100.0)
    assert isinstance(result, TransferResponse)
    assert result.transactionId == "tx-123"
    assert result.status == "SUCCESS"
