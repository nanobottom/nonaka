#include "iodefine.h"
#include "led.h"
/*
 * @brief LEDモジュールを初期化する。オレンジLEDとグリーンLEDを消灯状態とする。
 * @param (void)
 * @return (void)
 */
void Led_init(void){

	/* LED(オレンジ)を消灯する */
	IO.PDR6.BIT.B0 = 1;

	/* LED(グリーン)を消灯する*/
	IO.PDR6.BIT.B4 = 1;
}

/*
 * @brief 引数で指定したLEDに対して点灯・消灯状態を変化させる
 * @param (kind) LEDの色種別を指定する
 * @param (onoff) LEDの状態を指定する
 * @return 0:正常終了/ -1:異常終了（制御失敗）
 */
int Led_setLight(int kind, int onoff){
	if (kind == D_LED_KIND_ORANGE){
		/* オレンジLEDが消灯する場合 */
		if (onoff == D_LED_LIGHT_OFF){
			IO.PDR6.BIT.B0 = 1;
		/* オレンジLEDが点灯する場合 */
		}else if (onoff == D_LED_LIGHT_ON){
			IO.PDR6.BIT.B0 = 0;
		}else{
			return -1;
		}
	
	}else if(kind == D_LED_KIND_GREEN){
		/* 緑LEDが消灯する場合 */
		if (onoff == D_LED_LIGHT_OFF){
			IO.PDR6.BIT.B4 = 1;
		/* 緑LEDが点灯する場合 */
		}else if (onoff == D_LED_LIGHT_ON){
			IO.PDR6.BIT.B4 = 0;
		}else{
			return -1;
		}
	}else{
		return -1;
	}
	return 0;
}

