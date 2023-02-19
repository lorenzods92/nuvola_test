from pyntcloud import PyntCloud
import numpy as np
import pandas as pd
import open3d as o3d
from crea_punti import crea_punti




def main(pts):
    # pts = np.random.randint(0, 100, (100, 3))

    # whether to write in binary or text format
    write_text = True

    # use open3d
    use_o3d(pts, write_text)

    #calcola volume
    calc_volume('random.ply')

def use_o3d(pts, write_text):
    pcd = o3d.geometry.PointCloud()

    # the method Vector3dVector() will convert numpy array of shape (n, 3) to Open3D format.
    # see http://www.open3d.org/docs/release/python_api/open3d.utility.Vector3dVector.html#open3d.utility.Vector3dVector
    pcd.points = o3d.utility.Vector3dVector(pts)

    # http://www.open3d.org/docs/release/python_api/open3d.io.write_point_cloud.html#open3d.io.write_point_cloud
    o3d.io.write_point_cloud("random.ply", pcd, write_ascii=write_text)

    # read ply file
    pcd = o3d.io.read_point_cloud('random.ply')

    #visualize
    o3d.visualization.draw_geometries([pcd])
    
#main()

def calc_volume(filename):
    pass
    shape = PyntCloud.from_file(filename)
    convex_hull_id = shape.add_structure("convex_hull")
    convex_hull = shape.structures[convex_hull_id]
    #shape.mesh = convex_hull.get_mesh()
    print("calcolo volume")
    volume = convex_hull.volume
    
    print("volume", volume)
    
    #test
    from pyntcloud.geometry.models.sphere import create_sphere
    cloud = PyntCloud(create_sphere(center=[0, 0, 0], radius=25, n_points=100000))
    convex_hull_id = cloud.add_structure("convex_hull")
    convex_hull = cloud.structures[convex_hull_id]
    print(convex_hull.volume)

# diamond = PyntCloud.from_file("ipad2.ply")

# convex_hull_id = diamond.add_structure("convex_hull")
# convex_hull = diamond.structures[convex_hull_id]
# diamond.mesh = convex_hull.get_mesh()
# volume = convex_hull.volume

# # read ply file
# pcd = o3d.io.read_point_cloud('ipad2.ply')
# #visualize
# o3d.visualization.draw_geometries([pcd])

# from pyntcloud.geometry.models.sphere import create_sphere
# cloud = PyntCloud(create_sphere(center=[0, 0, 0], radius=25, n_points=100000))
# convex_hull_id = cloud.add_structure("convex_hull")
# convex_hull = cloud.structures[convex_hull_id]
# print(convex_hull.volume)

if __name__ == "__main__":
    pts = crea_punti()
    main(pts)