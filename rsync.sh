for grp in PIG_027 PIG_030 PIG_035 PIG_037 PIG_040 PIG_044 PIG_048 PIG_054 PIG_066 PIG_086;
do
rsync \
--filter='+ /FOFGroups/***' \
--filter='+ /4/***' \
--filter='+ /5/***' \
--filter='+ /header/***' \
--filter='- /**' \
-arL warp.hpc1.cs.cmu.edu:/physics2/yfeng1/BWSim/bluetide/$grp/  $grp/
done
