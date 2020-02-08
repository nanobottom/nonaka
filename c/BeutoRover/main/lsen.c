#include <stdio.h>
#include "iodefine.h"
#include "lsen.h"

/*
 * @brief 初期化
 * @param none
 * @return none
 */
void Lsen_init(void){
	/* スキャンモードとして単一モードを設定 */
	AD.ADCSR.BIT.SCAN = 0;
	/* クロックセレクトは134ステートを設定 */
	AD.ADCSR.BIT.CKS = 0;
	/* A/Dインタラプトイネーブルは割り込みを利用しないため0を設定 */
	AD.ADCSR.BIT.ADIE = 0;
	/* A/D変換をストップさせるため0を設定 */
	AD.ADCSR.BIT.ADST = 0;
}

/*
 * @brief 光センサーのAD値取得
 * @param sen1 センサー1に関するAD値(0-1023)
 * @param sen2 センサー2に関するAD値(0-1023)
 * @retval 0  正常
 *         -1 異常
 */
int Lsen_getSensor(unsigned short * sen1, unsigned short * sen2){
	/* NULLチェック */
	if ( sen1 == NULL || sen2 == NULL){
		return -1;
	}
	
	/**************************************************
	 * 光センサー1のAD変換処理
	 **************************************************/
	AD.ADCSR.BIT.CH = 0; // 変換チャネル指定
	AD.ADCSR.BIT.ADST = 1; //AD変換スタート

	/* AD変換完了待ち */
	while (AD.ADCSR.BIT.ADF == 0){
	};

	AD.ADCSR.BIT.ADF = 0; // 完了フラグクリア
	*sen1 = AD.ADDRA >> 6; // AD値取得

	/**************************************************
	 * 光センサー2のAD変換処理
	 **************************************************/
	AD.ADCSR.BIT.CH = 1; // 変換チャネル指定
	AD.ADCSR.BIT.ADST = 1; //AD変換スタート

	/* AD変換完了待ち */
	while (AD.ADCSR.BIT.ADF == 0){
	};

	AD.ADCSR.BIT.ADF = 0; // 完了フラグクリア
	*sen2 = AD.ADDRB >> 6; // AD値取得

	return 0;
}
