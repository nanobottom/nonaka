#include "iodefine.h"
#include "timer.h"

volatile static unsigned long g_system_time = 0;
/*
 * @brief 初期化。起動後時間の管理を開始する。
 * @param none
 * @return none
 */
void Timer_init(void){
	/* タイマモードレジスタB1(TMB1)の設定をする 
	 * ・オートリロード機能
	 * ・64分周
	 */
	//TB1.TMB1 = 0x84;
	TB1.TMB1.BIT.RLD = 1; // オートリロード機能有効
	TB1.TMB1.BIT.CKS = 4; // 分周Φ/64を選択
	/* タイマロードレジスタB1(TLB1)の設定をする
	 * リロード値設定 256 - 187 = 69
	 */
	//TLB1 = 69;
	TB1.TCB1 = 256 - 187; // リロードカウント値
	/* オーバーフロー割り込みをイネーブルにする */
	//IENR2.IENTB1 = 1;
	IENR2.BIT.IENTB1 = 1;
}

/*
 * @brief 起動後時間の取得
 * @param none
 * @return 起動後時間（単位：ms）
 */
unsigned long Timer_getTime(void){
	return g_system_time;
}

/*
 * @brief 指定時間待ち
 * @param msec 待ちたい時間（単位：ms）
 * @return none
 */
void Timer_waitTime(unsigned long msec){
	/* 呼び出し開始時刻を保持する */
	unsigned long time_now = g_system_time;
	while(1){
		/* 指定した時刻を過ぎたらループを抜ける */
		if (g_system_time - time_now >= msec){
			break;
		}
	}
}

/*
 * @brief オーバーフロー割り込み（1ms間隔で割り込みハンドラからコールされる）
 * @param none
 * @return none
 */
void Timer_interruptHandler(void){
	// システム時刻を1ms経過
	g_system_time++;
	/* 割り込み要求フラグをクリアする */
	IRR2.BIT.IRRTB1 = 0;
}

