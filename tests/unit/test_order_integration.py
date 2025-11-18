from src.order_io import load_order, write_receipt
from src.pricing import format_currency, bulk_total


def test_order_integration(tmp_path):
    input_file = tmp_path / "order.csv"
    input_file.write_text(
        "Apple,$1.50\nBanana,2.00\n",
        encoding="utf-8"
    )

    items = load_order(input_file)

    output_file = tmp_path / "receipt.txt"
    write_receipt(output_file, items, discount_percent=0, tax_rate=0.1)

    output_text = output_file.read_text(encoding="utf-8")

    assert "Apple: $1.50" in output_text
    assert "Banana: $2.00" in output_text

    assert "TOTAL:" in output_text
