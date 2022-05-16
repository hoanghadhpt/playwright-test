import { test, expect } from '@playwright/test';

test('test visible text and screenshot', async ({ page }) => {

  // 
  await page.goto('https://google.com/');
  let dateTime = new Date()
  // Check if visible text=
  await page.fill('#q','query');
  await page.screenshot({ path: 'screenshot_'+dateTime+'.png'});

});

test('test containt text', async ({ page }) => {

    // 
    await page.goto('https://vnexpress.net/');
  
  });