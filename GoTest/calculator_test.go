package calculator

import "testing"

func TestAdd(t *testing.T) {
	calc := Calculator{}
	result := calc.Add(2, 3)
	expected := 5

	if result != expected {
		t.Errorf("Add(2, 3) = %d; want %d", result, expected)
	}
}

func TestSubtract(t *testing.T) {
	calc := Calculator{}
	result := calc.Subtract(5, 3)
	expected := 2

	if result != expected {
		t.Errorf("Subtract(5, 3) = %d; want %d", result, expected)
	}
}

func TestMultiply(t *testing.T) {
	calc := Calculator{}
	result := calc.Multiply(4, 3)
	expected := 12

	if result != expected {
		t.Errorf("Multiply(4, 3) = %d; want %d", result, expected)
	}
}

func TestDivide(t *testing.T) {
	calc := Calculator{}
	result, err := calc.Divide(10, 2)

	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}

	expected := 5.0
	if result != expected {
		t.Errorf("Divide(10, 2) = %f; want %f", result, expected)
	}
}

func TestDivideByZero(t *testing.T) {
	calc := Calculator{}
	_, err := calc.Divide(10, 0)

	if err == nil {
		t.Error("Expected error for division by zero, got nil")
	}

	expectedMsg := "cannot divide by zero"
	if err.Error() != expectedMsg {
		t.Errorf("Expected error message '%s', got '%s'", expectedMsg, err.Error())
	}
}

func TestAddNegative(t *testing.T) {
	calc := Calculator{}
	result := calc.Add(-2, -3)
	expected := -5

	if result != expected {
		t.Errorf("Add(-2, -3) = %d; want %d", result, expected)
	}
}

func TestWithZero(t *testing.T) {
	calc := Calculator{}

	if calc.Add(0, 5) != 5 {
		t.Error("Add with zero failed")
	}

	if calc.Multiply(5, 0) != 0 {
		t.Error("Multiply with zero failed")
	}
}
