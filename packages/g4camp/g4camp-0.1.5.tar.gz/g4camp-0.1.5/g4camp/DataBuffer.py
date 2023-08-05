import numpy as np

class DataBuffer():

  def __init__(self):
    self.vertices_per_bunch = 10000
    self.vertex_bunces = 1
    self.vertex_num = 0
    self.vertices = np.zeros((self.vertices_per_bunch, 9), dtype=float)
    # 'vertex' row: pdgid, x[m], y[m], z[m], t[ns], Px[GeV], Py[GeV], Pz[GeV], Etot[GeV]
    #
    self.track_points_per_bunch = 100000
    self.track_point_bunches = 1
    self.point_num = 0
    self.tracks = np.zeros((self.track_points_per_bunch, 7), dtype=float) 
    # 'track' row:  uid, pdgid, x[m], y[m], z[m], t[ns], Etot[GeV]
    self.photon_cloud = []
    self.status = 'empty' # 'empty' -> 'in_progress' -> 'ready'

  def AddVertex(self, pdgid, x, y, z, t, Px, Py, Pz, Etot):
    self.status = 'in_progress'
    self.vertices[self.vertex_num] = [pdgid, x, y, z, t, Px, Py, Pz, Etot]
    self.vertex_num += 1
    if self.vertex_num % self.vertices_per_bunch == 0:
      self.vertices = np.concatenate((self.vertices, np.zeros((self.vertices_per_bunch, 9), dtype=int)))
      self.vertex_bunces += 1

  def AddPhoton(self, photon):
    self.status = 'in_progress'
    self.photon_cloud.append(photon)

  def AddTrackPoint(self, uid, pdgid, x, y, z, t, Etot):
    self.status = 'in_progress'
    self.tracks[self.point_num] = [uid, pdgid, x, y, z, t, Etot]
    self.point_num += 1
    if self.point_num % self.track_points_per_bunch == 0:
      self.tracks = np.concatenate((self.tracks, np.zeros((self.track_points_per_bunch, 7), dtype=int)))
      self.track_point_bunches += 1

  def CutEmptyItems(self):
    self.tracks = self.tracks[:self.point_num]
    self.vertices = self.vertices[:self.vertex_num]

  def SortItems(self):
    self.tracks = self.tracks[np.lexsort((self.tracks[:,5], self.tracks[:,0]))]

  def Clear(self):
    self.__init__()

  def Close(self):
    self.status = 'ready'

  def IsEmpty(self):
    return self.status == 'empty'

  def IsReady(self):
    return self.status == 'ready'

