#ifndef INCLUDED_LED_H_
#define INCLUDED_LED_H_

/*****************************************
 * マクロ定義
 *****************************************/

/* LED色種別の定数定義 */
#define D_LED_KIND_ORANGE (0) //オレンジLED
#define D_LED_KIND_GREEN (1) //グリーンLED

/* LED状態の定数定義 */
#define D_LED_LIGHT_OFF (0) //LED消灯
#define D_LED_LIGHT_ON (1) //LED点灯

/*****************************************
 * 型定義
 *****************************************/


/*****************************************
 * プロトタイプ宣言
 *****************************************/
void Led_init(void);
int Led_setLight(int kind, int onoff);

#endif //INCLUDED_LED_H_
