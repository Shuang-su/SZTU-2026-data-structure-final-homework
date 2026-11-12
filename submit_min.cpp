#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;typedef long long i;
#define j(b,y) for(int b=0;b<(int)(y);b++)
char bA[1<<16],ac[1<<22];int bB,bC;int bD(){if(bB==bC){bC=read(0,bA,sizeof bA);bB=0;if(bC<=0)return-1;}return bA[bB++];}int ax(){int d=bD(),y=0;while(d==' '||d=='\n'||d=='\r')d=bD();
while(d>' ')ac[y++]=d,d=bD();ac[y]=0;return y;}i e(){ax();return atoll(ac);}int aL,bE,bF,V,bG,W,cm,cn,co,cp,cq,l;i aM,aN,E,aO,ay,X[8];struct a9{vector<int>h;
i bH,aP;int bI;char K[400];};a9 ad[30],az[360];int Y[30],ba[30];int am[360],cr[360],cs[360],bb[360],bc[360],aQ[360];vector<int>an[360];i ct[360][602];int bd[1000],be[1000],ao[1000],bf[1000],bJ[8],aR=1;
vector<int>bK[600];i ap[30][30];int ae[200],bL[200];i aA[200],bg[200],bM[200],bN[200],bO[200];double cu[602],cv[602];vector<pair<int,i>>bh;int aq[400];
vector<int>bi[120];int cw[20][2],bP;vector<array<int,8>>C;vector<i>aB;struct B{int D,af,d,L,s,ar,p,as,aS,z,aT,aC,aD,bQ,bj,G;int at,cx,aU;double cy,bR,bS;
vector<int>M,bk;};struct S{int D,ag,ah,bT,first,y,aV,aW,cZ,aX,aY,aZ,c0;double a0;i u;};vector<B>k;vector<S>H;unordered_map<int,int>bl;string Z;i bm;int cz[360];
bool cA(a9&d,int v){if(!d.K[v])return 0;d.h.erase(find(d.h.begin(),d.h.end(),v));d.h.push_back(v);return 1;}void cB(a9&d,int v){d.h.push_back(v);d.K[v]=1,d.bI++;
d.aP+=aq[v];while(d.aP>d.bH){int r=d.h[0];d.aP-=aq[r];d.K[r]=0;d.h.erase(d.h.begin());}}i bU[30][600];char a1[30];void cC(){static int h[1024];static char K[600];
int cD=bF/bE;j(f,V)if(a1[f]){i*n=bU[f];j(b,bF)n[b]=1e18;int p=ba[f],N=0,O=0;if(!bJ[p/cD])n[p]=0,h[O++]=p;while(N!=O){int t=h[N++&1023];K[t]=0;for(int s:bK[t]){
int u=bd[s]^be[s]^t;if(bf[s]&&!bJ[u/cD]&&n[t]+ao[s]<n[u]){n[u]=n[t]+ao[s];if(!K[u])K[u]=1,h[O++&1023]=u;}}}j(w,V)ap[f][w]=n[ba[w]]>9e17?-1:n[ba[w]];a1[f]=0;
}aR=0;}double cE,cF,bV,bW,bX[602],bY[602],bZ[602];double cG(int r){return bZ[r];}void cH(){double c1=(cE+bV+100.*1.5)/(cF+bW+100.);j(r,W)bZ[r]=(cu[r]+bX[r]+30.*c1)/(cv[r]+bY[r]+30.);
}void bn(int o){B&a=k[o];int g=a.aT,r=H[a.af].ag;i F=a.d*X[Y[am[g]]];bb[g]+=a.d;bc[g]+=a.L;cz[g]=l;H[a.af].aZ=1;an[g].erase(find(an[g].begin(),an[g].end(),o));
bM[r]+=F*(l-a.aC);bN[r]-=F;bO[r]-=F*a.aC;for(int f=r;f>=0;f=ae[f])bg[f]-=a.d;a.z=0;a.G=l,a.aU=0;}i b0(int f,int w){return f==w?0:ap[f][w]<0?99:ap[f][w];
}bool cI(B&a,int m,i&aE,i&a2,i&b1){aE=a2=b1=0;int q=a.M.size();for(int b=a.p<0?0:-1;b<q;b++){int p=b<0?a.p:k[a.M[b]].bQ;i cJ=b<0?a.as:k[a.M[b]].aS;if(p==m)continue;
i n=ap[m][p];if(n<0)return 0;aE=max(aE,n+(cJ+E-1)/E);a2+=cJ*n*ay;if(b>=0)b1=max(b1,n);}return 1;}void cK(int o,int g){B&a=k[o];int m=am[g],r=H[a.af].ag;
i aE,a2,bo,ai=0,a3=0;cI(a,m,aE,a2,bo);for(int v:bi[a.ar]){if(cA(az[g],v))continue;if(cA(ad[m],v))a3+=aq[v];else ai+=aq[v],cB(ad[m],v);cB(az[g],v);}i F=a.d*X[Y[m]];
a.aD=max(aE,(ai+aM-1)/aM+(a3+aN-1)/aN);a.z=1;a.aT=g;a.aC=l;bb[g]-=a.d;bc[g]-=a.L;an[g].push_back(o);bM[r]+=bm=a2+ai*aO;bN[r]+=F;bO[r]+=F*l;for(int f=r;
f>=0;f=ae[f])bg[f]+=a.d;Z+="RUN "+to_string(a.D)+" "+to_string(g)+"\n";}i c2(int o){S&c=H[k[o].af];static i aF[1<<16],aG[1<<16];i F=0;j(b,c.y){B&a=k[c.first+b];
aF[b]=0;aG[b]=0;if(a.z>1)continue;for(int x:a.M)if(k[x].z<2)aF[b]=max(aF[b],aF[x-c.first]+k[x].s);F=max(F,aF[b]+a.s);}for(int b=c.y-1;b>=0;b--){B&a=k[c.first+b];
if(a.z>1)continue;aG[b]+=a.s;for(int x:a.M)aG[x-c.first]=max(aG[x-c.first],aG[b]);}return F-aF[o-c.first]-aG[o-c.first];}double a4[1<<17],b2[1<<17],au[1<<17],b3=3,b4=1,b5=50;
vector<pair<double,i>>aj[360];int b6[360],b7[360];vector<int>cL[30];double cM(S&c,double ak){i a5=max(5,(c.ah-c.bT)/3);if(ak<=c.ah)return c.u;if(ak>=c.ah+a5)return 0;
return c.u*(c.ah+a5-ak)/a5;}void c3(S&c,double&P,double&a6,double&Q){static double T[1<<16],aa[1<<16];double ak=cG(c.ag);i c4=X[Y[c.aY]];P=a6=Q=0;j(b,c.y){
B&a=k[c.first+b];T[b]=aa[b]=0;if(a.z>1)continue;for(int x:a.M)T[b]=max(T[b],T[x-c.first]+aa[x-c.first]);aa[b]=a.z?a4[c.first+b]-l:a.s*ak+1.*b3+a.bR;a6+=a.d*aa[b];
if(!a.z)aa[b]+=0.*b4;Q+=a.z?a.d*aa[b]*X[Y[am[a.aT]]]:a.d*aa[b]*c4+b5+a.bS;P=max(P,T[b]+aa[b]);au[c.first+b]=0;}i a5=max(5,(c.ah-c.bT)/3);for(int b=c.y-1;
b>=0;b--){int o=c.first+b;B&a=k[o];if(a.z>1)continue;au[o]+=aa[b];for(int x:a.M)au[x]=max(au[x],au[o]);double cN=T[b]+au[o],g=(l+cN-c.ah)/(1.*cN+1)+1;b2[o]=5.*a.d+c.u*1.0/a5*min(1.0,max(0.0,g));
}}void c5(S&c){double al=1e18;j(N,V){double a7=0;j(b,c.y){B&a=k[c.first+b];i F=a.d*X[Y[N]],n=a.p<0||a.p==N?0:ap[N][a.p];a7+=F*a.s;if(n<0)a7+=1e9;if(n>0)a7+=a.as*n*ay+(n+(a.as+E-1)/E)*(F+5.*a.d);
}if(a7<al)al=a7,c.aY=N;}j(b,c.y){B&a=k[c.first+b];i n=a.p<0||a.p==c.aY?0:ap[c.aY][a.p];if(n<0)n=60;a.bR=n?n+(a.as+E-1)/E:0,a.bS=a.as*n*ay;}}double c6(int g,int d,int L,double c7){
int b8=b6[g],b9=b7[g];if(b8>=d&&b9>=L)return 0;for(auto&h:aj[g]){if(h.first-l>c7)break;b8+=h.second>>32,b9+=int(h.second);if(b8>=d&&b9>=L)return h.first-l;
}return 1e9;}void ca(int g,int o,double end){b6[g]-=k[o].d,b7[g]-=k[o].L;pair<double,i>u(end,i(k[o].d)<<32|k[o].L);aj[g].insert(lower_bound(aj[g].begin(),aj[g].end(),u),u);
}void c8(int o){B&a=k[o];S&c=H[a.af];for(int f=c.ag;f>=0;f=ae[f])if(bg[f]+a.d>aA[f]){return;}if(a.aU>l&&(a.at<0||(aQ[a.at]&&cz[a.at]<a.cx))){if(a.at>=0)ca(a.at,o,a.cy);
return;}double bp=max(1.0,a.s*cG(c.ag)),al=1e18,aH=b2[o],av=0,cb=0;int aw=-1,cO=0;static i aI[30],cc[30];static double cd[30];static vector<pair<double,int>>I;
I.clear();j(m,V){i bo;if(cI(a,m,aI[m],cc[m],bo)){static i c9[120][30];static int cP[120][30];i&h=c9[a.ar][m];if(cP[a.ar][m]!=ad[m].bI+1){cP[a.ar][m]=ad[m].bI+1,h=0;
for(int v:bi[a.ar])if(!ad[m].K[v])h+=aq[v];}cd[m]=1.*h*aO;pair<double,int>u={cd[m]+cc[m]+aH*(aI[m]+1.*bo*!a.bk.empty())+a.d*X[Y[m]]*(aI[m]+bp),m};int q=I.size();
if(q<12.)I.push_back(u);else if(u.first<I[--q].first);else continue;for(;q&&u.first<I[q-1].first;q--)I[q]=I[q-1];I[q]=u;}}if(1.>0){static int aJ[8][5],a8[8];
static i aK[8][5];static double bq[8][5],ce[8][5];int A=0,cf[8];for(int cQ:a.bk){B&p=k[cQ];int q=0;if(p.p>=0)aJ[A][q]=p.p,aK[A][q++]=p.as;for(int x:p.M)if(x!=o&&q<5&&(k[x].z||1.>0)){
B*h=&k[x];for(int cR=0;cR<3&&!h->z&&h->p<0&&h->M.size();cR++)h=&k[h->M[0]];aJ[A][q]=h->z>1?h->bQ:h->z?am[h->aT]:h->p<0?c.aY:h->p,aK[A][q++]=k[x].aS;}if(!q||A>7)continue;
j(f,q){bq[A][f]=ce[A][f]=0;j(w,q){i n=b0(aJ[A][f],aJ[A][w]);if(n)bq[A][f]=max(bq[A][f],double(n+(aK[A][w]+E-1)/E)),ce[A][f]+=aK[A][w]*n;}}a8[A]=q,cf[A++]=cQ;
}if(A){for(auto&U:I){int m=U.second;j(b,A){double cS=b2[cf[b]]+k[cf[b]].d*X[Y[m]],cg=0,cT=0;j(f,a8[b]){i n=b0(m,aJ[b][f]);if(n)cg=max(cg,double(n+(aK[b][f]+E-1)/E)),cT+=aK[b][f]*n;
}double ch=cS*cg+ay*cT;j(f,a8[b]){i n=b0(m,aJ[b][f]);ch=min(ch,cS*max(n?double(n+(a.aS+E-1)/E):0,bq[b][f])+ay*(a.aS*n+ce[b][f]));}U.first+=1.*ch;}}sort(I.begin(),I.end());
}}for(auto&U:I){int m=U.second;U.first-=cd[m];if(U.first>=al)continue;for(int g:cL[m]){if(!aQ[g]||cr[g]<a.d||cs[g]<a.L)continue;double R=c6(g,a.d,a.L,(al-U.first)/(aH+1e-9));
if(U.first+aH*R>=al)continue;i ai=0,a3=0;for(int v:bi[a.ar])if(!az[g].K[v])(ad[m].K[v]?a3:ai)+=aq[v];i p=max(aI[m],(ai+aM-1)/aM+(a3+aN-1)/aN);double Q=U.first+ai*aO+(a.d*X[Y[m]]+aH)*(p-aI[m])+aH*R;
double cU=U.first+ai*aO+cc[m]+aH*R;int cV=1.>0&&cU<Q;if(cV)Q=cU,p=aI[m];if(Q<al)al=Q,aw=g,av=R,cb=p,cO=cV;}}a.cx=l,a.at=-1,a.aU=l+3.;if(aw<0||av>30.)return;
if(av>0){a.at=aw,a.cy=l+av+cb+bp,a.aU=l+min(4.,av*.5);ca(aw,o,l+av+cb+bp);return;}int da=a.G;i cW=0;if(cO&&!av){cK(o,aw);cW=bm;Z+="KILL "+to_string(a.D)+"\n";
bn(o);a.G=da;}cK(o,aw);bm+=cW;c.aX=c.aZ=1;b3=b3*.98+.02*max(0.0,a.aD-a.bR);b4=b4*.98+.02*min(12.,double(l-a.G));b5=b5*.98+.02*(bm-a.bS);a4[o]=l+a.aD+bp;
ca(aw,o,a4[o]);}void db(){double cX=clock()*1./CLOCKS_PER_SEC,ci=cX-.08-.62*l/aL;if(cX>.93||(ci>0&&l%(1<<min(5,int(ci/.04)))))return;cH();bV=bW=0;j(b,W)bX[b]=bY[b]=0;
j(g,bG){b6[g]=bb[g],b7[g]=bc[g];aj[g].clear();for(int h:an[g]){double br=max(0,l-k[h].aC-k[h].aD);int r=H[k[h].af].ag;if(br>k[h].s*bZ[r])bV+=br,bX[r]+=br,bW+=k[h].s,bY[r]+=k[h].s;
aj[g].push_back({a4[h]=max(l+1+.25*br,a4[h]),i(k[h].d)<<32|k[h].L});}sort(aj[g].begin(),aj[g].end());}cH();vector<pair<double,int>>bs;j(cj,H.size()){S&c=H[cj];
if(c.aW||!c.aV)continue;if(c.aZ||(ci<0&&(l+cj)%int(6.)==0)){double P,a6,Q,bt=0;c3(c,P,a6,Q);static const double bu[5]={-1,-.5,0,1,2};P*=1+.03*log(c.aV);
j(q,5){double ak=l+P*(1+.4*bu[q]);if(ak<=aL+30.||!1.)bt+=cM(c,ak)/5;}if(!1.&&l+P>aL)bt=0;c.aZ=0,c.a0=1;if(bt>Q*(c.aX?1.:1+0.)){c.a0=-(bt-Q)/(a6+1)*(c.aX?3.:1)/(1+1.*max(0.0,(c.ah-l-P)/P));
}else if(c.aX){c.aW=1;j(b,c.y)if(k[c.first+b].z==1){Z+="KILL "+to_string(k[c.first+b].D)+"\n";bn(c.first+b);}}else if(cM(c,l+P*.6)<=0)c.aW=1;}if(c.a0<0&&!c.aW)bs.push_back({
c.a0,cj});}sort(bs.begin(),bs.end());for(auto&r:bs){S&c=H[r.second];static vector<pair<double,int>>G;G.clear();j(b,c.y){B&a=k[c.first+b];if(a.z==0&&a.bj==0)G.push_back({
-au[c.first+b],c.first+b});}sort(G.begin(),G.end());for(auto&h:G)c8(h.second);}}int main(){aL=e(),bE=e(),bF=e(),V=e(),bG=e(),W=e();cm=e(),cn=e(),co=e(),cp=e(),cq=e();
aM=e(),aN=e(),E=e(),aO=e(),ay=e();j(b,bE)X[b]=e();j(b,V)Y[b]=e(),ba[b]=e(),ad[b].bH=e();j(b,bG){am[b]=e(),bb[b]=cr[b]=e(),bc[b]=cs[b]=e();az[b].bH=e(),aQ[b]=1;
cL[am[b]].push_back(b);}j(b,cq){bd[b]=e(),be[b]=e(),ao[b]=e(),bf[b]=1;bK[bd[b]].push_back(b),bK[be[b]].push_back(b);}j(b,W)ae[b]=e(),aA[b]=e();{int cY=0;
vector<char>ck(W);while(cY<W)j(b,W)if(!ck[b]&&(ae[b]<0||ck[ae[b]]))ck[b]=1,bL[cY++]=b;}j(b,cm)aq[b]=e();j(b,cn){int q=e();while(q--)bi[b].push_back(e());
}{i R[20];char bv[20]={};j(b,9)R[b]=e(),bv[b]=1;for(int D=9;D<17;D++){int cl[2];j(q,2){int w=-1;j(b,D)if(bv[b]&&(w<0||R[b]<R[w]))w=b;bv[w]=0,cl[q]=w;cw[D][q]=w;
}R[D]=R[cl[0]]+R[cl[1]],bv[D]=1;}bP=16;}{C.push_back(array<int,8>());aB.push_back(0);j(b,co){int y=ax(),t=0;j(q,y){int d=ac[q]-'a';if(!C[t][d])C[t][d]=C.size(),C.push_back(array<int,8>()),aB.push_back(0);
t=C[t][d];}aB[t]+=e();}vector<int>bw(C.size()),bx;j(d,8)if(C[0][d])bx.push_back(C[0][d]);j(dc,bx.size()){int t=bx[dc];aB[t]+=aB[bw[t]];j(d,8){int u=C[t][d];
if(u)bw[u]=C[bw[t]][d],bx.push_back(u);else C[t][d]=C[bw[t]][d];}}}j(f,V)a1[f]=1;for(;;){if(!ax())break;l=e();int dd=e(),a8=e();while(dd--){ax();string J=ac;
if(J=="DONE"){int o=bl[e()];B&a=k[o];S&c=H[a.af];int r=c.ag;cu[r]+=l-a.aC-a.aD,cv[r]+=a.s,cE+=l-a.aC-a.aD,cF+=a.s;bn(o);a.z=2;a.bQ=am[a.aT];for(int p:a.bk)k[p].bj--,k[p].G=l;
c.aV--;if(!c.aV)c.cZ=l;}else if(J=="FAIL"){int g=e();while(an[g].size())bn(an[g][0]);aQ[g]=0;a9&d=az[g];d.h.clear(),d.aP=0;memset(d.K,0,400);}else if(J=="UP"){
int g=e();aQ[g]=1;}else if(J=="DCDOWN"||J=="DCUP"){bJ[e()]=J.size()>4,aR=1;j(f,V)a1[f]=1;}else if(J=="LDOWN"||J=="LUP"){int s=e(),t=bd[s],u=be[s];bf[s]=J.size()<4,aR=1;
j(f,V){i g=bU[f][t],by=bU[f][u];if(bf[s]?g+ao[s]<by||by+ao[s]<g:g+ao[s]==by||by+ao[s]==g)a1[f]=1;}}else if(J=="QUOTA"){int O=e();bh.push_back({O,aA[O]}
);aA[O]=e();}else if(J=="UNDO"){int q=e();while(q--)aA[bh.back().first]=bh.back().second,bh.pop_back();}else if(J=="LOG"){int g=e(),w=e(),t=bP,T=0;ax();
i bu=0;j(b,w){int N=ac[b/4],de=((N<='9'?N-'0':(N|32)-'a'+10)>>(3-b%4))&1;t=cw[t][de];if(t<9){T=t<8?C[T][t]:0;bu+=aB[T];t=bP;}}ct[g][l]+=bu;}else{S c;c.D=e(),c.ag=e(),c.u=e(),c.ah=e(),c.y=c.aV=e();
c.bT=l,c.first=k.size(),c.aW=c.aX=c.c0=0,c.aZ=1,c.a0=1;j(b,c.y){B a;a.D=e(),a.d=e(),a.L=e(),a.s=e(),a.ar=e();a.p=e(),a.as=e(),a.aS=e(),a.bj=e();a.z=0,a.af=H.size(),a.G=l,a.aU=0;
j(q,a.bj){int x=bl[e()];a.M.push_back(x);k[x].bk.push_back(k.size());}bl[a.D]=k.size();k.push_back(a);}if(aR)cC();c5(c);H.push_back(c);}}if(aR)cC();Z="ANS";
while(a8--){ax();char h=ac[0],df=ac[1];int f=e();i ab=0;if(h=='B'){static i bz[200];j(b,W)bz[b]=bM[b]+bN[b]*l-bO[b];for(int b=W-1;b>0;b--)bz[ae[bL[b]]]+=bz[bL[b]];
ab=bz[f];}else if(h=='H'){ab=1e18;for(;f>=0;f=ae[f])ab=min(ab,aA[f]-bg[f]);}else if(h=='R'&&df=='O')ab=ap[f][e()];else if(h=='A'){for(int O=max(1,l-cp+1);
O<=l;O++)ab+=ct[f][O];}else if(h=='S')ab=c2(bl[f]);else ab=(h=='C'?az[f]:ad[f]).aP;Z+=" "+to_string(ab);}Z+="\n";db();Z+="END\n";fwrite(Z.data(),1,Z.size(),stdout);
fflush(stdout);if(l==aL)break;}}
