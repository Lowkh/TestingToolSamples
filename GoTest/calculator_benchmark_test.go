package calculator

import "testing"

func BenchmarkAdd(b *testing.B) {
	calc := Calculator{}
	for i := 0; i < b.N; i++ {
		calc.Add(100, 200)
	}
}

func BenchmarkMultiply(b *testing.B) {
	calc := Calculator{}
	for i := 0; i < b.N; i++ {
		calc.Multiply(500, 7)
	}
}

func BenchmarkDivide(b *testing.B) {
	calc := Calculator{}
	for i := 0; i < b.N; i++ {
		calc.Divide(100, 2)
	}
}

// Table-driven benchmark
func BenchmarkAddVariants(b *testing.B) {
	calc := Calculator{}
	tests := []struct {
		name string
		a, b int
	}{
		{"small", 1, 2},
		{"medium", 1000, 2000},
		{"large", 1000000, 2000000},
	}

	for _, tt := range tests {
		b.Run(tt.name, func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				calc.Add(tt.a, tt.b)
			}
		})
	}
}
