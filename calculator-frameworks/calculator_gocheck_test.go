package calculator

import (
	"testing"

	. "gopkg.in/check.v1"
)

// Hook gocheck into go test
func Test(t *testing.T) { TestingT(t) }

// Define test suite
type CalculatorCheckSuite struct {
	calc *Calculator
}

// Register the suite
var _ = Suite(&CalculatorCheckSuite{})

// SetUpSuite runs once before all tests
func (s *CalculatorCheckSuite) SetUpSuite(c *C) {
	c.Log("Setting up Calculator Suite")
}

// TearDownSuite runs once after all tests
func (s *CalculatorCheckSuite) TearDownSuite(c *C) {
	c.Log("Tearing down Calculator Suite")
}

// SetUpTest runs before each test
func (s *CalculatorCheckSuite) SetUpTest(c *C) {
	s.calc = NewCalculator()
}

// TearDownTest runs after each test
func (s *CalculatorCheckSuite) TearDownTest(c *C) {
	s.calc = nil
}

// Test methods
func (s *CalculatorCheckSuite) TestAdd(c *C) {
	// Assert stops test on failure
	c.Assert(s.calc.Add(2, 3), Equals, 5)

	// Check continues after failure
	c.Check(s.calc.Add(0, 5), Equals, 5)
	c.Check(s.calc.Add(-2, 3), Equals, 1)
}

func (s *CalculatorCheckSuite) TestSubtract(c *C) {
	c.Assert(s.calc.Subtract(5, 3), Equals, 2)
	c.Assert(s.calc.Subtract(3, 5), Equals, -2)
}

func (s *CalculatorCheckSuite) TestMultiply(c *C) {
	c.Assert(s.calc.Multiply(2, 3), Equals, 6)
	c.Assert(s.calc.Multiply(0, 10), Equals, 0)
	c.Assert(s.calc.Multiply(-2, 4), Equals, -8)
}

func (s *CalculatorCheckSuite) TestDivide(c *C) {
	result, err := s.calc.Divide(10, 2)
	c.Assert(err, IsNil)
	c.Assert(result, Equals, 5.0)
}

func (s *CalculatorCheckSuite) TestDivideByZero(c *C) {
	_, err := s.calc.Divide(10, 0)
	c.Assert(err, NotNil)
	c.Assert(err, ErrorMatches, "division by zero")
}

// Using different checkers
func (s *CalculatorCheckSuite) TestVariousCheckers(c *C) {
	// DeepEquals for complex types
	slice1 := []int{1, 2, 3}
	slice2 := []int{1, 2, 3}
	c.Assert(slice1, DeepEquals, slice2)

	// HasLen
	c.Assert(slice1, HasLen, 3)

	// Not
	c.Assert(5, Not(Equals), 6)
}

// Using Commentf for custom messages
func (s *CalculatorCheckSuite) TestWithComments(c *C) {
	input1, input2 := 2, 3
	result := s.calc.Add(input1, input2)
	c.Assert(result, Equals, 5,
		Commentf("Failed to add %d and %d", input1, input2))
}

// Skipping tests
func (s *CalculatorCheckSuite) TestSkipped(c *C) {
	c.Skip("This test is not ready yet")
	c.Assert(1, Equals, 2) // Won't run
}

// Using temporary directories
func (s *CalculatorCheckSuite) TestWithTempDir(c *C) {
	tmpDir := c.MkDir() // Automatically cleaned up
	c.Log("Created temp dir:", tmpDir)
	// Use tmpDir for file operations
}

// Benchmark in gocheck
func (s *CalculatorCheckSuite) BenchmarkAdd(c *C) {
	for i := 0; i < c.N; i++ {
		s.calc.Add(100, 200)
	}
}
