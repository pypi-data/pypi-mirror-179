from ispcr.utils import reverse_complement
import re


# def common_data(list1, list2):
#     result = False
#     for x in list1:
#         for y in list2:
#             if x == y:
#                 result = True
#                 return result

#     return result


def get_product(fpri, rpri, se, name):
    product = ""
    psize = 0
    pfpri = ""
    prpri = ""
    for x in fpri:  # x is the key of the dict fpri, x is the sequence
        ma = [m.start() for m in re.finditer(x, se)]
        if len(ma) > 0:
            for st in ma:
                tempseq = se[st:]
                for y in rpri:
                    rma = [m.start() for m in re.finditer(y, tempseq)]
                    if len(rma) > 0:
                        # build an array based on x's forward primer cluster ID, [c001, c002, ...]
                        fpri_li = fpri[x].split(",")
                        for i, ff in enumerate(fpri_li):
                            f = ff.split(".")[-2]
                            fpri_li[i] = f
                            # print(fpri_li)

                        # build an array based on y's reverse primer cluster ID, [c001, c002, ...]
                        rpri_li = rpri[y].split(",")
                        for j, rr in enumerate(rpri_li):
                            r = rr.split(".")[-2]
                            rpri_li[j] = r
                        # print(rpri_li)

                        for rst in rma:
                            # check if there're at least one pair of forward and reverse primers ID are from the same cluster
                            if common_data(fpri_li, rpri_li):
                                product = tempseq[: rst + len(y)]
                                psize = len(product)
                                if psize >= len(x) + len(y):
                                    pfpri = x
                                    prpri = y
                                    prim_pair = fpri[pfpri] + "=" + rpri[prpri]
                                    sim_name = name.split()[0]
                                    des = name.split()[1:]
                                    if len(des) > 0:
                                        descr = "_".join(des)
                                    else:
                                        descr = "_"
                                    print(
                                        ">{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
                                            sim_name,
                                            descr,
                                            fpri[pfpri],
                                            pfpri,
                                            rpri[prpri],
                                            reverse_complement(prpri),
                                            prim_pair,
                                            st,
                                            st + rst + len(y),
                                            psize,
                                        )
                                    )


# def find_product(fpri, rpri, file):
#     with open(file) as seqs:
#         name = ""
#         flag = 0
#         seq = []
#         for line in seqs:
#             if line[:1] == ">" and flag == 0:
#                 name = line.strip()[1:]
#                 flag = 1
#             elif line[:1] == ">" and flag == 1:
#                 se = "".join(seq).upper()
#                 get_product(fpri, rpri, se, name)
#                 name = line.strip()[1:]
#                 seq = []
#             else:
#                 seq.append(line.strip())
#         se = "".join(seq).upper()
#         get_product(fpri, rpri, se, name)

# def get_pcr_product(forward_primer)

# def read_primer(file):
#     with open(file) as prim:
#         fpri = {}
#         rpri = {}
#         name = ""
#         for line in prim:
#             if line[:1] == ">":
#                 ptype = line.strip()[1]
#                 nameL = line.strip().split(".")
#                 name = ptype + "." + nameL[-2] + "." + nameL[-1]
#             else:
#                 seq = line.strip()
#                 seq = seq.upper()
#                 rseq = reverse_complement(seq)
#                 if name[0] == "F":
#                     if seq in fpri:
#                         temp = fpri[seq] + "," + name
#                         fpri[seq] = temp
#                     else:
#                         fpri[seq] = name
#                 if name[0] == "R":
#                     if seq in rpri:
#                         temp = rpri[rseq] + "," + name
#                         rpri[rseq] = temp
#                     else:
#                         rpri[rseq] = name
#     return fpri, rpri


def main():
    # Read primers from primers.fa
    prim = sys.argv[1]
    fpri, rpri = read_primer(prim)

    # Find products of primers from sequences.fa
    seqs = sys.argv[2]
    find_product(fpri, rpri, seqs)
