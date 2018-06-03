#Sync the BT-ii data

for grp in PIG_092  PIG_095  PIG_105  PIG_121  PIG_129  PIG_136  PIG_141;
do
rsync \
--filter='+ /FOFGroups/***' \
--filter='+ /4/***' \
--filter='+ /5/***' \
--filter='+ /Header/***' \
--filter='- /**' \
--delete \
-arL coma.hpc1.cs.cmu.edu:/home/yfeng1/bluetides-ii/$grp/  $grp/
done
