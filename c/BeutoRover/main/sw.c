#include "iodefine.h"
#include "sw.h"

/*
 * @brief SWモジュールを初期化する
 * @param (void)
 * @return (void)
 */
void Sw_init(void){

}

/*
 * @brief スイッチ状態の取得
 * @param (void)
 * @return D_SW_PRESSED_OFF 押されていない
 *         D_SW_PRESSED_ON 押されている
 */
int Sw_getPressed(void){
	/* SWが押されていない場合 */
	if (IO.PDR7.BIT.B4 == 1){
		return D_SW_PRESSED_OFF;
	/* SWが押されている場合 */
	}else{
		return D_SW_PRESSED_ON;
	}
}
