# #slice score
#     if(volume.slice_distance > 0 and volume.slice_thickness > 0):
#         p = volume.slice_thickness / volume.slice_distance
#         # from f(x) = e^(-pi*(x-1)^2)
#         score_slice = np.exp(-np.pi * (p - 1)**2)
#     num_score = .0
#     if(vol_dim > 10):
#         num_score+= int(vol_dim/100) * 0.5 + int(vol_dim/50)*0.3 + 0.2
#     final_score = score_vol * 0.7 + score_slice * 0.3 + num_score
#     return [score_vol, score_slice, final_score]