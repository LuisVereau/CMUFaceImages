import os

def _convertIdtoInt(id):
    id_conv = -1
    if (id == 'an2i'):
        id_conv = 0
    if (id == 'at33'):
        id_conv = 1
    if (id == 'boland'):
        id_conv = 2
    if (id == 'bpm'):
        id_conv = 3
    if (id == 'ch4f'):
        id_conv = 4
    if (id == 'cheyer'):
        id_conv = 5
    if (id == 'choon'):
        id_conv = 6
    if (id == 'danieln'):
        id_conv = 7
    if (id == 'glickman'):
        id_conv = 8
    if (id == 'karyadi'):
        id_conv = 9
    if (id == 'kawamura'):
        id_conv = 10
    if (id == 'kk49'):
        id_conv = 11
    if (id == 'megak'):
        id_conv = 12
    if (id == 'mitchell'):
        id_conv = 13
    if (id == 'night'):
        id_conv = 14
    if (id == 'phoebe'):
        id_conv = 15
    if (id == 'saavik'):
        id_conv = 16
    if (id == 'steffi'):
        id_conv = 17
    if (id == 'sz24'):
        id_conv = 18
    if (id == 'tammo'):
        id_conv = 19
    return id_conv

def getFaces(dir):
    os.chdir(dir)
    imgs = list()
    for folder in os.listdir():
        os.chdir(folder)
        for img in os.listdir():
            if (img.split('_')[-1] != '4.pgm' and img.split('_')[-1] != '2.pgm'):
                # Images are 128 columns by 120 rows
                id = _convertIdtoInt(img.split('_')[0])
                path_aux = (os.getcwd()+f'\{img}').split('\\')[7:]
                path = '\\'.join(path_aux)
                imgs.append((path, id))
        os.chdir(dir)
    return imgs