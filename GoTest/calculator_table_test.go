package calculator

import "testing"

/*
func TestAddTableDriven(t *testing.T) {
	calc := Calculator{}

	tests := []struct {
		name     string
		a, b     int
		expected int
	}{
		{"positive numbers", 2, 3, 5},
		{"negative numbers", -2, -3, -5},
		{"with zero", 0, 5, 5},
		{"negative and positive", -2, 3, 1},
		{"large numbers", 1000000, 2000000, 3000000},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := calc.Add(tt.a, tt.b)
			if result != tt.expected {
				t.Errorf("Add(%d, %d) = %d; want %d",
					tt.a, tt.b, result, tt.expected)
			}
		})
	}
}*/

func TestMultiplyTableDriven(t *testing.T) {
	calc := Calculator{}

	tests := []struct {
		name     string
		a, b     int
		expected int
	}{
		{"positive numbers", 2, 3, 6},
		{"with zero", 0, 10, 0},
		{"negative and positive", -2, 4, -8},
		{"two negatives", -3, -4, 12},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := calc.Multiply(tt.a, tt.b)
			if result != tt.expected {
				t.Errorf("%s: Multiply(%d, %d) = %d; want %d",
					tt.name, tt.a, tt.b, result, tt.expected)
			}
		})
	}
}
