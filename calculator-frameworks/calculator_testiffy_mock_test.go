package calculator

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"
)

// Define an interface
type MathService interface {
	Calculate(operation string, a, b int) int
}

// Create mock
type MockMathService struct {
	mock.Mock
}

func (m *MockMathService) Calculate(operation string, a, b int) int {
	args := m.Called(operation, a, b)
	return args.Int(0)
}

// Example service that uses the interface
type CalculatorService struct {
	mathService MathService
}

func (cs *CalculatorService) PerformOperation(op string, a, b int) int {
	return cs.mathService.Calculate(op, a, b)
}

// Test using mock
func TestCalculatorServiceWithMock(t *testing.T) {
	mockService := new(MockMathService)

	// Set expectations
	mockService.On("Calculate", "add", 2, 3).Return(5)

	// Test
	calcService := &CalculatorService{mathService: mockService}
	result := calcService.PerformOperation("add", 2, 3)

	// Assertions
	assert.Equal(t, 5, result)
	mockService.AssertExpectations(t)
	mockService.AssertCalled(t, "Calculate", "add", 2, 3)
}
