ax = plt.subplot(111)

ax.set_title(objtitle)
ax.set_xlabel("$\psi$ ($\circ$)")
ax.set_ylabel("a (au)")
ax.set_xlim(0,360)
ax.set_xticks([0,60,120,180,240,300,360])

ax.set_ylim(ymin,ymax)


alltp = pd.read_csv(filename, header=None, index_col=False,skiprows=1,
                       names=["stab", "p", "q", "id", "t", "a", "psi", "e", "inc"])

#completed at least 1000 resonant cycles in full simulations
stable_particles = alltp[alltp["stab"]==1]
#completed at least 750 resonant cycles in full simulations
quasistable_particles = alltp[alltp["stab"]==2]
#did not librate for at least 750 cycles in original targeted resonance
#could still be in higher-order resonances, but mostly not
particles = alltp[alltp["stab"]==0]


#add resonance labels to the plot for anything with stable or quasi-stable 
#resonant particles
first_rows = quasistable_particles[quasistable_particles["t"]==0]
aresvals = []
for index, row in first_rows.iterrows():
    ares = np.power((row["p"]/row["q"]),(2./3.))*30.06
    if(ares < ymax and ares > ymin) and not(ares in aresvals):
        resl = str(int(row["p"])) + ":" + str(int(row["q"]))
        ax.text(365,ares,resl,fontsize='small')
        aresvals.append(ares)
first_rows = stable_particles[stable_particles["t"]==0]
for index, row in first_rows.iterrows():
    ares = np.power((row["p"]/row["q"]),(2./3.))*30.06
    if(ares < ymax and ares > ymin) and not(ares in aresvals):
        resl = str(int(row["p"])) + ":" + str(int(row["q"]))
        ax.text(365,ares,resl,fontsize='small')
        aresvals.append(ares)


#plot the particles:



ids = particles[particles["t"]==0].id
alreadyplotted = []
#point size and alpha
w = 0.2*pointsize
a = 0.6
for i in ids:
    #avoids duplicate plots since id numbers are repeated for different resonances
    if not(i in alreadyplotted):
        ax.plot(particles[particles["id"]==i].psi.to_numpy()*180./np.pi,
                particles[particles["id"]==i].a.to_numpy(),
                marker='o',linestyle='none',fillstyle='full',
                alpha=a,markersize=w,
                markeredgewidth=0,zorder=-10)
        alreadyplotted.append(i)


ids = quasistable_particles[quasistable_particles["t"]==0].id

alreadyplotted = []
#point size and alpha
w = 0.3*pointsize
a = 0.7
for i in ids:
    #avoids duplicate plots since id numbers are repeated for different resonances
    if not(i in alreadyplotted):
        ax.plot(quasistable_particles[quasistable_particles["id"]==i].psi.to_numpy()*180./np.pi,
                quasistable_particles[quasistable_particles["id"]==i].a.to_numpy(),
                marker='o',linestyle='none',fillstyle='full',
                alpha=a,markersize=w,
                markeredgewidth=0,zorder=-10)
        alreadyplotted.append(i)


ids = stable_particles[stable_particles["t"]==0].id

alreadyplotted = []
#point size and alpha
w = 0.5*pointsize
a = 0.9
for i in ids:
    #avoids duplicate plots since id numbers are repeated for different resonances
    if not(i in alreadyplotted):
        ax.plot(stable_particles[stable_particles["id"]==i].psi.to_numpy()*180./np.pi,
                stable_particles[stable_particles["id"]==i].a.to_numpy(),
                marker='o',linestyle='none',fillstyle='full',
                alpha=a,markersize=w,
                markeredgewidth=0,zorder=-10)
        alreadyplotted.append(i)

ax.set_rasterization_zorder(0)    

x=np.zeros(5)
y=np.zeros(5)
x = [obspsi,obspsi,obspsi,obspsi,obspsi]

y1=abf-3.*da
y2=abf-da
y3=abf
y4=abf+da
y5=abf+3.*da



y = [y1,y2,y3,y4,y5]
ax.plot(x,y,marker='o',linestyle='-',c='k')
plt.subplots_adjust(left=0.2, bottom=0.15, right=0.8, top=None, wspace=None, hspace=None)
fig.savefig(figfile,dpi=300)

