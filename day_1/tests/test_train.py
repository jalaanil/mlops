from datetime import date
from duration_prediction.train import train
from pathlib import Path
import tempfile


def test_val():
    assert 1==2

def test_regression():
    with tempfile.TemporaryDirectory() as tmpdir:
        #given
        train_date= date(2022,1,1)
        val_date = date( 2022,2,1)
        output_path = Path(tmpdir) / "model.bin"

        #when
        mse = train(train_date , val_date , output_path)

        #then
        assert abs( 18.18 - mse ) < 0.1 

