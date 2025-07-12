import pytest
from playwright.sync_api import Page, expect

@pytest.mark.e2e
def test_calculator_ui_addition(page: Page):
    
    page.goto("http://127.0.0.1:8000")
    page.fill("input[name='operand1']", "5")
    page.fill("input[name='operand2']", "3")
    page.select_option("select[name='operation']", "add")
    page.click("button[type='submit']")

    result_div = page.locator("#result")
    expect(result_div).to_have_text("Result: 8")