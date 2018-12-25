class math_geo:


    def __init__(self):
        pass

    # a faire avec l'image principale puis
    # les morceaux dimages

    def match_geo(self, dossier_depart):

        self.dossier_depart = dossier_depart
        

        matches_biatches = 600

        im1 = cv2.imread(self.image_a_compa, 0)
        im2 = cv2.imread(j, 0)

        orb = cv2.ORB_create()

        kp1, des1 = orb.detectAndCompute(im2, None)
        kp2, des2 = orb.detectAndCompute(im1, None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        matches = bf.match(des1,des2)
        matches = sorted(matches, key = lambda x:x.distance)

        im3 = cv2.drawMatches(im1,kp1,im2,kp2,
                              matches[:matches_biatches],
                              None, flags=2)
