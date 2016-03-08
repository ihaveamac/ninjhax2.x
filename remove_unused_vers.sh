VERS=("U_20480" "U_21504" "U_22528" "U_23554" "U_24576")
for v in ${VERS[@]}; do
	rm p/N3DS_${v}_9221.bin
	rm p/POST5_${v}_9221.bin
	rm q/N3DS_${v}_9221.png
	rm q/POST5_${v}_9221.png
	rm r/N3DS_${v}_9221.bin
	rm r/POST5_${v}_9221.bin
done