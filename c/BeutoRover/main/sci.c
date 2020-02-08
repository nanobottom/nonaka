#include <stdio.h>
#include "iodefine.h"
#include "sci.h"

/*
 * @brief 初期化
 * @param none
 * @return none
 */
void Sci_init(void){
	/* 通信モード設定。調歩同期式モードに設定する */
	SCI3.SMR.BIT.COM = 0:
	/* データ長:8bit */
	SCI3.SMR.BIT.CHR = 0;
	/* ビットレート:19200bps */
	SCI3.SMR.BIT.CKS1 = 0;
	SCI3.SMR.BIT.CKS0 = 0;
	SCI3.BRR = 19;
	/* パリティ:使用しない */
	SCI3.SMR.BIT.PE = 0;
	/* ストップビット長:1bit */
	SCI3.SMR.BIT.STOP = 0;
}

/*
 * @brief 文字の送信
 * @param moji 送信したい文字
 * @retval 0 正常
 *        -1 異常
 */
int Sci_putChar(char moji){
	/* 送信動作を開始する */
	SCI3.SCR3.TE = 1;

	if (SCI3.SSR.BIT.TDRE == 1){
		/* 送信データをライト */
		SCI3.TDR = moji;
	}

	/* 送信動作を停止する */
	SCI3.SCR3.TE = 0;

	return 0;
}

/*
 * @brief 文字列の送信
 * @param str 送信したい文字列
 * @retval 0 正常
 *        -1 異常
 */
int Sci_putString(char * str){

	/* NULLチェック */
	if (str == NULL){
		return -1;
	}
	/* 送信動作を開始する */
	SCI3.SCR3.TE = 1;

	printf("%s\n", str);

	/* 送信動作を停止する */
	SCI3.SCR3.TE = 0;

	return 0;

}
