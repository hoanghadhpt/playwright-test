import { test, expect } from '@playwright/test';

test('Testcase 1', async ({ page }) => {
  // Go to https://vnexpress.net/
  await page.goto('https://vnexpress.net/');
  // Click nav >> text=Thời sự >> nth=0
  await Promise.all([
    page.waitForNavigation(/*{ url: 'https://vnexpress.net/thoi-su' }*/),
    page.locator('nav >> text=Thời sự').first().click()
  ]);

  // Click text=Chính trị >> nth=4
  await Promise.all([
    page.waitForNavigation(/*{ url: 'https://vnexpress.net/thoi-su/chinh-tri' }*/),
    page.locator('text=Chính trị').first().click()
  ]);
  // Screenshot
  await page.screenshot({ path: 'screenshot.png', fullPage: true });
});