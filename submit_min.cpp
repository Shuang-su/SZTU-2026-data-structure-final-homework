#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;typedef long long i;
#define j(b,x) for(int b=0;b<(int)(x);b++)
char bv[1<<16],aa[1<<22];int bw,bx;int by(){if(bw==bx){bx=read(0,bv,sizeof bv);bw=0;if(bx<=0)return-1;}return bv[bw++];}int ar(){int d=by(),x=0;while(d==' '||d=='\n'||d=='\r')d=by();
while(d>' ')aa[x++]=d,d=by();aa[x]=0;return x;}i e(){ar();return atoll(aa);}int a5,bz,bA,R,bB,S,ci,cj,ck,cl,cm,l;i aG,aH,D,bC,as,T[8];struct a6{vector<int>h;
i bD,aI;char N[400];};a6 aJ[30],at[360];int U[30],a7[30];int ah[360],cn[360],co[360],a8[360],a9[360],aK[360];vector<int>ai[360];i cp[360][602];int ba[1000],bb[1000],aj[1000],bc[1000],bE[8],aL=1;
vector<int>bF[600];i ak[30][30];int ab[200],bG[200];i au[200],bd[200],bH[200],bI[200],bJ[200];double cq[602],cr[602];vector<pair<int,i>>be;int av[400];
vector<int>bK[120];int cs[20][2],bL;vector<array<int,8>>C;vector<i>aw;struct B{int E,ac,d,I,q,bM,o,al,aM,y,aN,ax,ay,bN,bf,V;int am,ct,aO;double cu,bO,bP;
vector<int>J,bg;};struct O{int E,ad,ae,bQ,first,x,aP,aQ,cR,aR,aS,aT,cS;double aU;i u;};vector<B>k;vector<O>G;unordered_map<int,int>bh;string af;i cv;int cw[360];
bool cx(a6&d,int z){if(!d.N[z])return 0;d.h.erase(find(d.h.begin(),d.h.end(),z));d.h.push_back(z);return 1;}void cy(a6&d,int z){d.h.push_back(z);d.N[z]=1;
d.aI+=av[z];while(d.aI>d.bD){int p=d.h[0];d.aI-=av[p];d.N[p]=0;d.h.erase(d.h.begin());}}i bR[30][600];char aV[30];void cz(){static int h[1024];static char N[600];
int cA=bA/bz;j(f,R)if(aV[f]){i*m=bR[f];j(b,bA)m[b]=1e18;int o=a7[f],K=0,L=0;if(!bE[o/cA])m[o]=0,h[L++]=o;while(K!=L){int r=h[K++&1023];N[r]=0;for(int q:bF[r]){
int u=ba[q]^bb[q]^r;if(bc[q]&&!bE[u/cA]&&m[r]+aj[q]<m[u]){m[u]=m[r]+aj[q];if(!N[u])N[u]=1,h[L++&1023]=u;}}}j(v,R)ak[f][v]=m[a7[v]]>9e17?-1:m[a7[v]];aV[f]=0;
}aL=0;}double cB,cC,bS,bT,bU[602],bV[602],bW[602];double cD(int p){return bW[p];}void cE(){double cT=(cB+bS+100.*1.5)/(cC+bT+100.);j(p,S)bW[p]=(cq[p]+bU[p]+30.*cT)/(cr[p]+bV[p]+30.);
}void bX(int n){B&a=k[n];int g=a.aN,p=G[a.ac].ad;i F=a.d*T[U[ah[g]]];a8[g]+=a.d;a9[g]+=a.I;cw[g]=l;G[a.ac].aT=1;ai[g].erase(find(ai[g].begin(),ai[g].end(),n));
bH[p]+=F*(l-a.ax);bI[p]-=F;bJ[p]-=F*a.ax;for(int f=p;f>=0;f=ab[f])bd[f]-=a.d;a.y=0;a.V=l,a.aO=0;}i bY(int f,int v){return f==v?0:ak[f][v]<0?99:ak[f][v];
}bool cF(B&a,int s,i&az,i&aW,i&bZ){az=aW=bZ=0;int t=a.J.size();for(int b=a.o<0?0:-1;b<t;b++){int o=b<0?a.o:k[a.J[b]].bN;i cG=b<0?a.al:k[a.J[b]].aM;if(o==s)continue;
i m=ak[s][o];if(m<0)return 0;az=max(az,m+(cG+D-1)/D);aW+=cG*m*as;if(b>=0)bZ=max(bZ,m);}return 1;}void cU(int n,int g){B&a=k[n];int s=ah[g],p=G[a.ac].ad;
i az,aW,bi,an=0,aX=0;cF(a,s,az,aW,bi);for(int z:bK[a.bM]){if(cx(at[g],z))continue;if(cx(aJ[s],z))aX+=av[z];else an+=av[z],cy(aJ[s],z);cy(at[g],z);}i F=a.d*T[U[s]];
a.ay=max(az,(an+aG-1)/aG+(aX+aH-1)/aH);a.y=1;a.aN=g;a.ax=l;a8[g]-=a.d;a9[g]-=a.I;ai[g].push_back(n);bH[p]+=cv=aW+an*bC;bI[p]+=F;bJ[p]+=F*l;for(int f=p;
f>=0;f=ab[f])bd[f]+=a.d;af+="RUN "+to_string(a.E)+" "+to_string(g)+"\n";}i cV(int n){O&c=G[k[n].ac];static i aA[1<<16],aB[1<<16];i F=0;j(b,c.x){B&a=k[c.first+b];
aA[b]=0;aB[b]=0;if(a.y>1)continue;for(int w:a.J)if(k[w].y<2)aA[b]=max(aA[b],aA[w-c.first]+k[w].q);F=max(F,aA[b]+a.q);}for(int b=c.x-1;b>=0;b--){B&a=k[c.first+b];
if(a.y>1)continue;aB[b]+=a.q;for(int w:a.J)aB[w-c.first]=max(aB[w-c.first],aB[b]);}return F-aA[n-c.first]-aB[n-c.first];}double aY[1<<17],b0[1<<17],ao[1<<17],b1=3,b2=1,b3=50;
vector<pair<double,i>>ag[360];int b4[360],b5[360];vector<int>cH[30];double cI(O&c,double aZ){i a0=max(5,(c.ae-c.bQ)/3);if(aZ<=c.ae)return c.u;if(aZ>=c.ae+a0)return 0;
return c.u*(c.ae+a0-aZ)/a0;}void cW(O&c,double&M,double&a1,double&W){static double P[1<<16],X[1<<16];double aZ=cD(c.ad);i cX=T[U[c.aS]];M=a1=W=0;j(b,c.x){
B&a=k[c.first+b];P[b]=X[b]=0;if(a.y>1)continue;for(int w:a.J)P[b]=max(P[b],P[w-c.first]+X[w-c.first]);X[b]=a.y?aY[c.first+b]-l:a.q*aZ+1.*b1+a.bO;a1+=a.d*X[b];
if(!a.y)X[b]+=1.*b2;W+=a.y?a.d*X[b]*T[U[ah[a.aN]]]:a.d*X[b]*cX+b3+a.bP;M=max(M,P[b]+X[b]);ao[c.first+b]=0;}i a0=max(5,(c.ae-c.bQ)/3);for(int b=c.x-1;b>=0;
b--){int n=c.first+b;B&a=k[n];if(a.y>1)continue;ao[n]+=X[b];for(int w:a.J)ao[w]=max(ao[w],ao[n]);double cJ=P[b]+ao[n],g=(l+cJ-c.ae)/(1.*cJ+1)+1;b0[n]=5.*a.d+c.u*1.0/a0*min(1.0,max(0.0,g));
}}void cY(O&c){double ap=1e18;j(K,R){double a2=0;j(b,c.x){B&a=k[c.first+b];i F=a.d*T[U[K]],m=a.o<0||a.o==K?0:ak[K][a.o];a2+=F*a.q;if(m<0)a2+=1e9;if(m>0)a2+=a.al*m*as+(m+(a.al+D-1)/D)*(F+5.*a.d);
}if(a2<ap)ap=a2,c.aS=K;}j(b,c.x){B&a=k[c.first+b];i m=a.o<0||a.o==c.aS?0:ak[c.aS][a.o];if(m<0)m=60;a.bO=m?m+(a.al+D-1)/D:0,a.bP=a.al*m*as;}}double cZ(int g,int d,int I){
int b6=b4[g],b7=b5[g];if(b6>=d&&b7>=I)return 0;for(auto&h:ag[g]){b6+=h.second>>32,b7+=int(h.second);if(b6>=d&&b7>=I)return h.first-l;}return 1e9;}void b8(int g,int n,double end){
b4[g]-=k[n].d,b5[g]-=k[n].I;pair<double,i>u(end,i(k[n].d)<<32|k[n].I);ag[g].insert(lower_bound(ag[g].begin(),ag[g].end(),u),u);}void c0(int n){B&a=k[n];
O&c=G[a.ac];for(int f=c.ad;f>=0;f=ab[f])if(bd[f]+a.d>au[f])return;if(a.aO>l&&(a.am<0||(aK[a.am]&&cw[a.am]<a.ct))){if(a.am>=0)b8(a.am,n,a.cu);return;}double bj=max(1.0,a.q*cD(c.ad)),ap=1e18,bk=b0[n],aC=0,b9=0;
int aD=-1;static i a3[30],cK[30];vector<pair<double,int>>Y;j(s,R){i bi;if(cF(a,s,a3[s],cK[s],bi))Y.push_back({cK[s]+bk*(a3[s]+1.*bi*!a.bg.empty())+a.d*T[U[s]]*(a3[s]+bj),s}
);}sort(Y.begin(),Y.end());if(Y.size()>6.)Y.resize(6.);if(1.>0){static int aE[8][5],a4[8];static i aF[8][5];static double bl[8][5],ca[8][5];int A=0,cb[8];
for(int cL:a.bg){B&o=k[cL];int t=0;if(o.o>=0)aE[A][t]=o.o,aF[A][t++]=o.al;for(int w:o.J)if(w!=n&&t<5&&(k[w].y||1.>0)){B*h=&k[w];for(int cM=0;cM<3&&!h->y&&h->o<0&&h->J.size();
cM++)h=&k[h->J[0]];aE[A][t]=h->y>1?h->bN:h->y?ah[h->aN]:h->o<0?c.aS:h->o,aF[A][t++]=k[w].aM;}if(!t||A>7)continue;j(f,t){bl[A][f]=ca[A][f]=0;j(v,t){i m=bY(aE[A][f],aE[A][v]);
if(m)bl[A][f]=max(bl[A][f],double(m+(aF[A][v]+D-1)/D)),ca[A][f]+=aF[A][v]*m;}}a4[A]=t,cb[A++]=cL;}if(A){for(auto&aq:Y){int s=aq.second;j(b,A){double cN=b0[cb[b]]+k[cb[b]].d*T[U[s]],cc=0,cO=0;
j(f,a4[b]){i m=bY(s,aE[b][f]);if(m)cc=max(cc,double(m+(aF[b][f]+D-1)/D)),cO+=aF[b][f]*m;}double cd=cN*cc+as*cO;j(f,a4[b]){i m=bY(s,aE[b][f]);cd=min(cd,cN*max(m?double(m+(a.aM+D-1)/D):0,bl[b][f])+as*(a.aM*m+ca[b][f]));
}aq.first+=1.*cd;}}sort(Y.begin(),Y.end());}}for(auto&aq:Y){if(aq.first>=ap)break;int s=aq.second;for(int g:cH[s]){if(!aK[g]||cn[g]<a.d||co[g]<a.I)continue;
double Q=cZ(g,a.d,a.I);if(aq.first+bk*Q>=ap)continue;i an=0,aX=0;for(int z:bK[a.bM])if(!at[g].N[z])(aJ[s].N[z]?aX:an)+=av[z];i o=max(a3[s],(an+aG-1)/aG+(aX+aH-1)/aH);
double W=aq.first+an*bC+(a.d*T[U[s]]+bk)*(o-a3[s])+bk*Q;if(W<ap)ap=W,aD=g,aC=Q,b9=o;}}a.ct=l,a.am=-1,a.aO=l+3.;if(aD<0||aC>30.)return;if(aC>0){a.am=aD,a.cu=l+aC+b9+bj,a.aO=l+min(4.,aC*.5);
b8(aD,n,l+aC+b9+bj);return;}cU(n,aD);c.aR=c.aT=1;b1=b1*.98+.02*max(0.0,a.ay-a.bO);b2=b2*.98+.02*min(12.,double(l-a.V));b3=b3*.98+.02*(cv-a.bP);aY[n]=l+a.ay+bj;
b8(aD,n,aY[n]);}void c1(){double cP=clock()*1./CLOCKS_PER_SEC,ce=cP-.08-.62*l/a5;if(cP>.93||(ce>0&&l%(1<<min(5,int(ce/.04)))))return;cE();bS=bT=0;j(b,S)bU[b]=bV[b]=0;
j(g,bB){b4[g]=a8[g],b5[g]=a9[g];ag[g].clear();for(int h:ai[g]){double bm=max(0,l-k[h].ax-k[h].ay);int p=G[k[h].ac].ad;if(bm>k[h].q*bW[p])bS+=bm,bU[p]+=bm,bT+=k[h].q,bV[p]+=k[h].q;
ag[g].push_back({aY[h]=max(l+1+.25*bm,aY[h]),i(k[h].d)<<32|k[h].I});}sort(ag[g].begin(),ag[g].end());}cE();vector<pair<double,int>>bn;j(cf,G.size()){O&c=G[cf];
if(c.aQ||!c.aP)continue;if(c.aT||(ce<0&&(l+cf)%int(6.)==0)){double M,a1,W,bo=0;cW(c,M,a1,W);static const double bp[5]={-1,-.5,0,1,2};M*=1+.03*log(c.aP);
j(t,5)bo+=cI(c,l+M*(1+.4*bp[t]))/5;if(l+M>a5)bo=0;c.aT=0,c.aU=1;if(bo>W*(c.aR?1.:1+0.)){c.aU=-(bo-W)/(a1+1)*(c.aR?3.:1)/(1+1.*max(0.0,(c.ae-l-M)/M));}else if(c.aR){
c.aQ=1;j(b,c.x)if(k[c.first+b].y==1){af+="KILL "+to_string(k[c.first+b].E)+"\n";bX(c.first+b);}}else if(cI(c,l+M*.6)<=0)c.aQ=1;}if(c.aU<0&&!c.aQ)bn.push_back({
c.aU,cf});}sort(bn.begin(),bn.end());for(auto&p:bn){O&c=G[p.second];vector<pair<double,int>>V;j(b,c.x){B&a=k[c.first+b];if(a.y==0&&a.bf==0)V.push_back({
-ao[c.first+b],c.first+b});}sort(V.begin(),V.end());for(auto&h:V)c0(h.second);}}int main(){a5=e(),bz=e(),bA=e(),R=e(),bB=e(),S=e();ci=e(),cj=e(),ck=e(),cl=e(),cm=e();
aG=e(),aH=e(),D=e(),bC=e(),as=e();j(b,bz)T[b]=e();j(b,R)U[b]=e(),a7[b]=e(),aJ[b].bD=e();j(b,bB){ah[b]=e(),a8[b]=cn[b]=e(),a9[b]=co[b]=e();at[b].bD=e(),aK[b]=1;
cH[ah[b]].push_back(b);}j(b,cm){ba[b]=e(),bb[b]=e(),aj[b]=e(),bc[b]=1;bF[ba[b]].push_back(b),bF[bb[b]].push_back(b);}j(b,S)ab[b]=e(),au[b]=e();{int cQ=0;
vector<char>cg(S);while(cQ<S)j(b,S)if(!cg[b]&&(ab[b]<0||cg[ab[b]]))cg[b]=1,bG[cQ++]=b;}j(b,ci)av[b]=e();j(b,cj){int t=e();while(t--)bK[b].push_back(e());
}{i Q[20];char bq[20]={};j(b,9)Q[b]=e(),bq[b]=1;for(int E=9;E<17;E++){int ch[2];j(t,2){int v=-1;j(b,E)if(bq[b]&&(v<0||Q[b]<Q[v]))v=b;bq[v]=0,ch[t]=v;cs[E][t]=v;
}Q[E]=Q[ch[0]]+Q[ch[1]],bq[E]=1;}bL=16;}{C.push_back(array<int,8>());aw.push_back(0);j(b,ck){int x=ar(),r=0;j(t,x){int d=aa[t]-'a';if(!C[r][d])C[r][d]=C.size(),C.push_back(array<int,8>()),aw.push_back(0);
r=C[r][d];}aw[r]+=e();}vector<int>br(C.size()),bs;j(d,8)if(C[0][d])bs.push_back(C[0][d]);j(c2,bs.size()){int r=bs[c2];aw[r]+=aw[br[r]];j(d,8){int u=C[r][d];
if(u)br[u]=C[br[r]][d],bs.push_back(u);else C[r][d]=C[br[r]][d];}}}j(f,R)aV[f]=1;for(;;){if(!ar())break;l=e();int c3=e(),a4=e();while(c3--){ar();string H=aa;
if(H=="DONE"){int n=bh[e()];B&a=k[n];O&c=G[a.ac];int p=c.ad;cq[p]+=l-a.ax-a.ay,cr[p]+=a.q,cB+=l-a.ax-a.ay,cC+=a.q;bX(n);a.y=2;a.bN=ah[a.aN];for(int o:a.bg)k[o].bf--,k[o].V=l;
c.aP--;if(!c.aP)c.cR=l;}else if(H=="FAIL"){int g=e();while(ai[g].size())bX(ai[g][0]);aK[g]=0;a6&d=at[g];d.h.clear(),d.aI=0;memset(d.N,0,400);}else if(H=="UP"){
int g=e();aK[g]=1;}else if(H=="DCDOWN"||H=="DCUP"){bE[e()]=H.size()>4,aL=1;j(f,R)aV[f]=1;}else if(H=="LDOWN"||H=="LUP"){int q=e(),r=ba[q],u=bb[q];bc[q]=H.size()<4,aL=1;
j(f,R){i g=bR[f][r],bt=bR[f][u];if(bc[q]?g+aj[q]<bt||bt+aj[q]<g:g+aj[q]==bt||bt+aj[q]==g)aV[f]=1;}}else if(H=="QUOTA"){int L=e();be.push_back({L,au[L]}
);au[L]=e();}else if(H=="UNDO"){int t=e();while(t--)au[be.back().first]=be.back().second,be.pop_back();}else if(H=="LOG"){int g=e(),v=e(),r=bL,P=0;ar();
i bp=0;j(b,v){int K=aa[b/4],c4=((K<='9'?K-'0':(K|32)-'a'+10)>>(3-b%4))&1;r=cs[r][c4];if(r<9){P=r<8?C[P][r]:0;bp+=aw[P];r=bL;}}cp[g][l]+=bp;}else{O c;c.E=e(),c.ad=e(),c.u=e(),c.ae=e(),c.x=c.aP=e();
c.bQ=l,c.first=k.size(),c.aQ=c.aR=c.cS=0,c.aT=1,c.aU=1;j(b,c.x){B a;a.E=e(),a.d=e(),a.I=e(),a.q=e(),a.bM=e();a.o=e(),a.al=e(),a.aM=e(),a.bf=e();a.y=0,a.ac=G.size(),a.V=l,a.aO=0;
j(t,a.bf){int w=bh[e()];a.J.push_back(w);k[w].bg.push_back(k.size());}bh[a.E]=k.size();k.push_back(a);}if(aL)cz();cY(c);G.push_back(c);}}if(aL)cz();af="ANS";
while(a4--){ar();char h=aa[0],c5=aa[1];int f=e();i Z=0;if(h=='B'){static i bu[200];j(b,S)bu[b]=bH[b]+bI[b]*l-bJ[b];for(int b=S-1;b>0;b--)bu[ab[bG[b]]]+=bu[bG[b]];
Z=bu[f];}else if(h=='H'){Z=1e18;for(;f>=0;f=ab[f])Z=min(Z,au[f]-bd[f]);}else if(h=='R'&&c5=='O')Z=ak[f][e()];else if(h=='A'){for(int L=max(1,l-cl+1);L<=l;
L++)Z+=cp[f][L];}else if(h=='S')Z=cV(bh[f]);else Z=(h=='C'?at[f]:aJ[f]).aI;af+=" "+to_string(Z);}af+="\n";c1();af+="END\n";fwrite(af.data(),1,af.size(),stdout);
fflush(stdout);if(l==a5)break;}}
