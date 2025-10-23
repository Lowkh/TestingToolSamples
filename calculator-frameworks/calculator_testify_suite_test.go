package calculator

import (
	"testing"

	"github.com/stretchr/testify/suite"
)

// Define test suite
type CalculatorSuite struct {
	suite.Suite
	calc *Calculator
}

// SetupSuite runs once before all tests
func (s *CalculatorSuite) SetupSuite() {
	s.T().Log("Setting up Calculator Suite")
}

// TearDownSuite runs once after all tests
func (s *CalculatorSuite) TearDownSuite() {
	s.T().Log("Tearing down Calculator Suite")
}

// SetupTest runs before each test
func (s *CalculatorSuite) SetupTest() {
	s.calc = NewCalculator()
	s.T().Log("Created new calculator")
}

// TearDownTest runs after each test
func (s *CalculatorSuite) TearDownTest() {
	s.calc = nil
	s.T().Log("Cleaned up calculator")
}

// Test methods must start with "Test"
func (s *CalculatorSuite) TestAdd() {
	result := s.calc.Add(2, 3)
	s.Equal(5, result)
	s.Greater(result, 4)
}

func (s *CalculatorSuite) TestSubtract() {
	s.Equal(2, s.calc.Subtract(5, 3))
	s.Equal(-2, s.calc.Subtract(3, 5))
}

func (s *CalculatorSuite) TestMultiply() {
	s.Equal(6, s.calc.Multiply(2, 3))
	s.Equal(0, s.calc.Multiply(0, 5))
}

func (s *CalculatorSuite) TestDivide() {
	result, err := s.calc.Divide(10, 2)
	s.NoError(err)
	s.Equal(5.0, result)
}

func (s *CalculatorSuite) TestDivideByZero() {
	_, err := s.calc.Divide(5, 0)
	s.Error(err)
	s.Contains(err.Error(), "division by zero")
}

// Run the suite
func TestCalculatorSuite(t *testing.T) {
	suite.Run(t, new(CalculatorSuite))
}
