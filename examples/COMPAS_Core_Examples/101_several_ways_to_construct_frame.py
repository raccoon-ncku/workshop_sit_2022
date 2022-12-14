"""There are several ways to construct a `Frame`.
"""
import compas.geometry as cg

# Frame autocorrects axes to be orthonormal
F = cg.Frame(cg.Point(1, 0, 0), cg.Vector(-0.45, 0.1, 0.3), cg.Vector(1, 0, 0))

F = cg.Frame([1, 0, 0], [-0.45, 0.1, 0.3], [1, 0, 0])

F = cg.Frame.from_points([1, 1, 1], [2, 3, 6], [6, 3, 0])
F = cg.Frame.from_plane(cg.Plane([0, 0, 0], [0.5, 0.2, 0.1]))
F = cg.Frame.from_euler_angles([0.5, 1., 0.2])
F = cg.Frame.worldXY()
