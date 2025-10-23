package calculator

import (
	"testing"

	"github.com/franela/goblin"
)

func TestGoblinFixed(t *testing.T) {
	g := goblin.Goblin(t)

	g.Describe("Calculator Operations", func() {
		var calc *Calculator

		g.BeforeEach(func() {
			calc = NewCalculator()
		})

		g.Describe("Addition", func() {
			g.It("adds positive numbers", func() {
				result := calc.Add(2, 3)
				g.Assert(result).Eql(5)
			})

			g.It("adds negative numbers", func() {
				result := calc.Add(-2, -3)
				g.Assert(result).Eql(-5)
			})
		})

		g.Describe("Division", func() {
			g.It("divides correctly", func() {
				result, err := calc.Divide(10, 2)
				g.Assert(err == nil).IsTrue()
				g.Assert(result).Eql(5.0)
			})

			g.It("errors on division by zero", func() {
				_, err := calc.Divide(10, 0)
				g.Assert(err != nil).IsTrue()
			})
		})
	})
}
