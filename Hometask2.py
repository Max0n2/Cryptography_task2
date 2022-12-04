import ECPoint as ECP

p1 = ECP.ECPoint(0, 2)
p1.PrintECPoint()
print(p1.ECPointToString(), "- точка яка є еліптичній кривій" if p1.IsOnCurveCheck() else "- точка яка не є еліптичній кривій")

p2 = ECP.ECPoint(-1, 0)
p2.PrintECPoint()
print(p2.ECPointToString(), "- точка яка є еліптичній кривій" if p2.IsOnCurveCheck() else "- точка яка не є еліптичній кривій")

p3 = ECP.AddECPoints(p1, p2)
p3.PrintECPoint()
print(p3.ECPointToString(), "- точка яка є еліптичній кривій" if p3.IsOnCurveCheck() else "- точка яка не є еліптичній кривій")

p4 = p3.DoubleECPoint()
p4.PrintECPoint()
print(p4.ECPointToString(), "- точка яка є еліптичній кривій" if p4.IsOnCurveCheck() else "- точка яка не є еліптичній кривій")

p5 = p3.ScalarMult(3)
p5.PrintECPoint()
print(p5.ECPointToString(), "- точка яка є еліптичній кривій" if p5.IsOnCurveCheck() else "- точка яка не є еліптичній кривій")