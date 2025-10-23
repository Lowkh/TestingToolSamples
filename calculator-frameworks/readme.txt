# To run all tests
# Standard Go test (includes all frameworks)
go test -v

# Run only Testify tests
go test -v -run Testify

# Run only gocheck tests
go test -v -run Check

# Run only Goblin tests
go test -v -run Goblin


# To run specific tests
# Testify suite
go test -v -run TestCalculatorSuite

# gocheck specific test
go test -check.f CalculatorCheckSuite.TestAdd

# Goblin nested test
go test -v -run TestGoblinNested

# To run with coverage
go test -cover
go test -coverprofile=coverage.out
go tool cover -html=coverage.out
