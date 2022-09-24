--bf_output.lua--
r1=259.8
r2=260.2
dr=0.1

z1=-209.8
z2=210.2
dz=0.1

ni = (r2-r1)/dr+1
nj = (z2-z1)/dz+1

handle=openfile("B_field_map_conductor.dat","w")
write(handle,"COLUMNS = r z B Br Bz ")
write(handle,format("ZONE I=%d J=%d \n",ni,nj))

for j=0,nj-1,1 do
  for i=0,ni-1,1 do
  r=r1+i*dr
  z=z1+j*dz
  A,Br,Bz=mo_getpointvalues(r,z)
  write(handle,r," ",z," ",sqrt(Br*Br+Bz*Bz)," ",Br," ",Bz,"\n")
 end
end

closefile(handle)
