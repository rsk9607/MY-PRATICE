n,k,l,c,d,p,nl,np = [int(x) for x in input().split()]
drink = l*k
slices = c*d
salt = p
dirnk_req = drink//nl
salt_requied = salt//np
print(min(dirnk_req,salt_requied,slices)//n)