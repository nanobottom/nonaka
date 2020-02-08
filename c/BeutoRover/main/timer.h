#ifndef INCLUDED_TIMER_H_
#define INCLUDED_TIMER_H_

/**************************************************
 * マクロ定義
 **************************************************/

/**************************************************
 * 型定義
 **************************************************/

/**************************************************
 * プロトタイプ宣言
 **************************************************/
void Timer_init(void);
unsigned long Timer_getTime(void);
void Timer_waitTime(unsigned long msec);
void Timer_interruptHandler(void);


#endif //INCLUDED_TIMER_H_
