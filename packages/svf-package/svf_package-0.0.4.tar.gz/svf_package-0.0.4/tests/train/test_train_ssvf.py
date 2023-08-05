from svf_package.svf_functions import create_SVF
from tests import data


if __name__ == '__main__':

    inputs = [["x1"],["x1","x2"],["x1","x2","y1"]]
    outputs = [["y1"]]
    prediccion = [[3],[1,2],[1,3,1]]
    c = 1
    eps = 0
    d = 2
    method_list = ["SVF","SSVF","dual","SVF-SP"]
    for i in inputs:
        cont = len(i)-1
        for o in outputs:
            for method in method_list:
                print("N_INP:", i," N_OUT:", o)
                svf = create_SVF(method, i, o, data, c, eps, d)
                svf.train()
                # print(svf.model.export_to_string())
                svf.solve()
                print(method, svf.solution.w, "=>", svf.get_estimation(prediccion[cont]))
                print("***********************************************************")
    print("=======================================================================")

