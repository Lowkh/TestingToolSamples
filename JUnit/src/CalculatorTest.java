import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Calculator Tests")
class CalculatorTest {

    private Calculator calculator;

    @BeforeEach
    void setUp() {
        calculator = new Calculator();
        System.out.println("Setting up calculator...");
    }

    @Test
    @DisplayName("Test addition")
    void testAdd() {
        int result = calculator.add(2, 3);
        assertEquals(5, result, "2 + 3 should equal 5");
    }

    @Test
    @DisplayName("Test subtraction")
    void testSubtract() {
        int result = calculator.subtract(5, 3);
        assertEquals(2, result, "5 - 3 should equal 2");
    }

    @Test
    @DisplayName("Test multiplication")
    void testMultiply() {
        int result = calculator.multiply(4, 3);
        assertEquals(12, result, "4 * 3 should equal 12");
    }

    @Test
    @DisplayName("Test division")
    void testDivide() {
        double result = calculator.divide(10, 2);
        assertEquals(5.0, result, "10 / 2 should equal 5");
    }

    @Test
    @DisplayName("Test division by zero")
    void testDivideByZero() {
        Exception exception = assertThrows(
            IllegalArgumentException.class,
            () -> calculator.divide(10, 0)
        );
        
        String expectedMessage = "Cannot divide by zero";
        String actualMessage = exception.getMessage();
        
        assertTrue(actualMessage.contains(expectedMessage));
    }

    @Test
    @DisplayName("Test adding negative numbers")
    void testAddNegative() {
        int result = calculator.add(-2, -3);
        assertEquals(-5, result, "-2 + -3 should equal -5");
    }

    @Test
    @DisplayName("Test with zero")
    void testWithZero() {
        assertEquals(5, calculator.add(0, 5));
        assertEquals(0, calculator.multiply(5, 0));
    }
}
