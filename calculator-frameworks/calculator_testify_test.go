package calculator

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestAddWithTestify(t *testing.T) {
	calc := NewCalculator()

	// assert continues on failure
	assert.Equal(t, 5, calc.Add(2, 3), "2 + 3 should equal 5")
	assert.NotEqual(t, 6, calc.Add(2, 3))
}

func TestSubtractWithTestify(t *testing.T) {
	calc := NewCalculator()
	assert := assert.New(t)

	assert.Equal(2, calc.Subtract(5, 3))
	assert.Equal(-2, calc.Subtract(3, 5))
}

func TestMultiplyWithTestify(t *testing.T) {
	calc := NewCalculator()
	assert := assert.New(t)

	assert.Equal(6, calc.Multiply(2, 3))
	assert.Equal(0, calc.Multiply(0, 10))
	assert.Equal(-8, calc.Multiply(-2, 4))
}

func TestDivideWithTestify(t *testing.T) {
	calc := NewCalculator()

	result, err := calc.Divide(10, 2)
	assert.NoError(t, err)
	assert.Equal(t, 5.0, result)
}

func TestDivideByZeroWithTestify(t *testing.T) {
	calc := NewCalculator()

	_, err := calc.Divide(10, 0)
	assert.Error(t, err)
	assert.EqualError(t, err, "division by zero")
}

// Using require - stops test immediately on failure
func TestRequireExample(t *testing.T) {
	calc := NewCalculator()

	result, err := calc.Divide(10, 2)
	require.NoError(t, err, "Division should not error")

	// This line only runs if above passes
	assert.Equal(t, 5.0, result)
}
