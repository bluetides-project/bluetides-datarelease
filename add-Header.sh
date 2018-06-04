# older BT-I data uses header for the Header block
#
for i in PIG_???; do (cd $i; ln -T -s header Header) done

