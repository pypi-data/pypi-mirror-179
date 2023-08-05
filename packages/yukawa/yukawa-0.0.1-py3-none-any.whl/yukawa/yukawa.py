#!/usr/bin/env python3
r'''
Tools for chiral fermions
'''
import itertools


def remove_double_intersection_pairs(msvp, l):
    '''
    Example:
        msvp = [(3,4),(6,-13),(1,6),(-7,14),(1,-8)]
        l = [1, 3, 4, 6, -7, -8, -13, 14]
        # Remove (1,6) because is fully contained 
        # in the intersections with (_1_,-8) and (_6_,-13)
        returns: 
        [(3,4),(6,-13),(-7,14),(1,-8)]    
    '''
    for p in msvp.copy():
        tmp = msvp.copy()
        tmp.remove(p)
        fltmp = set([x for sublist in tmp for x in sublist])
        if l.count(p[0]) == 1 and l.count(p[1]) == 1 and set(p).issubset(fltmp):
            msvp = tmp.copy()
    return msvp
# TODO: Move to tests
assert len(remove_double_intersection_pairs([(-10, 11), (-12, 13), (11, -12)],
                                             [-10, 11, -12, 13]))==2
assert len(remove_double_intersection_pairs([(4,4),(4,-12)],[4,-12]))==1

def get_real_massless(l,msvp):
    '''
    Example:
        l = [1, 3, 4, 6, -7, -8, -13, 14]
        msvp = [(3,4),(6,-13),(-7,14),(1,-8)]
        [1, 3, 4, 6, -7, -8, -13, 14] → [(3,4),(6,-13),(-7,14),(1,-8)]
        [1, 6, -7, -8, -13, 14] → [(6,-13),(-7,14),(1,-8)]
        [1, -7, -8, 14] → [(-7,14),(1,-8)]
        [1, -8] → [(1,-8)]
        [] → []
        
        returns:
        [] # lp    
    '''
    lp = l.copy()
    for x, y in msvp:
        #print(lp,msvp,x,y)
        if lp and x in lp and y in lp:
            minxy = min(lp.count(x), lp.count(y))
            if x != y:
                [(lp.remove(x), lp.remove(y)) for ii in range(minxy)]
            else:
                [lp.remove(x) for ii in range(lp.count(x))]  # abs(2*x)==s
        else:  # not lp
            break
    return lp


def get_massive_fermions(l,s,ps=[]):
    '''
    For a given scalar Abelian charge `s`, build the 
    fermion non-zero determinant mass matrix from their
    Abelian charges in `l`, and returns the input `s` and 
    the non-zero mass entries.
    Returns an empty dictionary otherwise.
    
    The list of combinations on pairs of `l` can be given in `ps`,
    otherwise it is internally calculated.
    
    Example:
        l = [1, 3, 4, 6, -7, -8, -13, 14]
        s = 7
        ps = [(3,4),(6,-13),(1,6),(-7,14),(1,-8)]
        # If necessary temove [1,6] because have is fully contained 
        # in the intersections with others
        [1, 3, 4, 6, -7, -8, -13, 14] → [(3,4),(6,-13),(-7,14),(1,-8)]
        [1, 6, -7, -8, -13, 14] → [(6,-13),(-7,14),(1,-8)]
        [1, -7, -8, 14] → [(-7,14),(1,-8)]
        [1, -8] → [(1,-8)]
        [] → []
        
        returns:
        {'s':7, '\psi':[(3,4),(6,-13),(1,6),(-7,14),(1,-8)]}

    '''
    sltn={}
    if not ps:
        ps = list(set(itertools.combinations_with_replacement(l,2)))
    msv = [p for p in ps if abs(sum(p))==s]
    lmsv=[x for sublist in msv for x in sublist]
    massives=set(lmsv)        
    massless=set(l).difference(massives)
    if not massless:
        # ========= Quality check =======================
        # Check that all the elements of l can be removed
        for INTERSECTIONS in [False,True]:
            msvp=msv.copy()
            lp=l.copy()
            if INTERSECTIONS:
                msvp = remove_double_intersection_pairs(msvp,l)
            for msvp in itertools.permutations(msvp.copy()):
                msvp=list(msvp)
                lp=get_real_massless(l,msvp)
                if not lp:
                    break # found real massless
            if not lp: # double break for INTERSECTIONS
                break # found real massless
                    
        
        if not lp:
            sltn['S']=s
            sltn['ψ']=msv
        return sltn

# TODO: Move to tests
assert get_massive_fermions([2, 4, 4, 5, 5, 7],9).get('S')==9          

if __name__ == '__main__':
    r'''
    Checks
    '''
    print(get_massive_fermions([1, 3, 4, 6, -7, -8, -13, 14],7))
