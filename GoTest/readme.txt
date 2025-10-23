# Run all tests
go test
# Run tests and see what's happening (verbose)
go test -v
# Run only TestAdd
go test -run TestAdd
# Run only TestSubtract
go test -run TestSubtract
# Run only TestMultiply
go test -run TestMultiply
# Run only TestDivide
go test -run TestDivide
# Verbose (see details)
go test -v -run TestAdd
# Run table-driven test
go test -run TestAddTableDriven
# Run specific case in table-driven test
go test -run TestAddTableDriven/positive_numbers
go test -run TestAddTableDriven/negative_numbers
go test -run TestAddTableDriven/with_zero
# See all cases run
go test -v -run TestAddTableDriven
# Run all benchmarks
go test -bench=.
# Run specific benchmark
go test -bench=BenchmarkAdd
go test -bench=BenchmarkMultiply
# Show memory usage too
go test -bench=. -benchmem
# Run benchmark longer (more accurate)
go test -bench=. -benchtime=5s
# Basic coverage
go test -cover
# See which lines were tested
go test -coverprofile=coverage.out
go tool cover -func=coverage.out
# Create visual HTML report
go test -coverprofile=coverage.out
go tool cover -html=coverage.out
# Run Testify suite
go test -v -run TestCalculatorSuite
# Run specific test in suite
go test -v -run TestCalculatorSuite/TestAdd
# Run with gocheck verbose output
go test -check.v
# Run specific gocheck suite
go test -check.f CalculatorCheckSuite
# Run specific test
go test -check.f CalculatorCheckSuite.TestAdd
# Run Goblin BDD tests
go test -v -run TestCalculator

