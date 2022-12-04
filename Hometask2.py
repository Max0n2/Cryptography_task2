from ECurve import ECurve, ECPoint

curve = ECurve(3, 4)
print(curve.EquationToString())
curve.PrintEquation()

p1 = ECPoint(0, 2)
p1.PrintECPoint()
print(p1.ECPointToString(), "- точка яка є еліптичній кривій" if p1.IsOnCurveCheck(curve) else "- точка яка не є еліптичній кривій")

p2 = ECPoint(-1, 0)
p2.PrintECPoint()
print(p2.ECPointToString(), "- точка яка є еліптичній кривій" if p2.IsOnCurveCheck(curve) else "- точка яка не є еліптичній кривій")

p3 = curve.AddECPoints(p1, p2)
p3.PrintECPoint()
print(p3.ECPointToString(), "- точка яка є еліптичній кривій" if p3.IsOnCurveCheck(curve) else "- точка яка не є еліптичній кривій")
p4 = p3.DoubleECPoint(curve)
p4.PrintECPoint()
print(p4.ECPointToString(), "- точка яка є еліптичній кривій" if p4.IsOnCurveCheck(curve) else "- точка яка не є еліптичній кривій")

p5 = p3.ScalarMult(3)
p5.PrintECPoint()
print(p5.ECPointToString(), "- точка яка є еліптичній кривій" if p5.IsOnCurveCheck(curve) else "- точка яка не є еліптичній кривій")