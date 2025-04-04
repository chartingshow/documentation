# Houbi/HTX Exchange: Stop-Loss Limit Order

- [Houbi/HTX Exchange: Stop-Loss Limit Order](#houbi-htx-exchange--stop-loss-limit-order)
  - [How to set a stop-loss limit order on the Huobi HTX crypto exchange](#how-to-set-a-stop-loss-limit-order-on-the-huobi-htx-crypto-exchange)
    - [What is a Stop-Loss Limit Order?](#what-is-a-stop-loss-limit-order-)
    - [Steps to Set a Stop-Loss Limit Order](#steps-to-set-a-stop-loss-limit-order)
      - [1. Setting a Stop-Loss Limit When Opening a Position](#1-setting-a-stop-loss-limit-when-opening-a-position)
        - [On the Web Platform](#on-the-web-platform)
        - [On the Mobile App](#on-the-mobile-app)
      - [2. Setting a Stop-Loss Limit for an Existing Position](#2-setting-a-stop-loss-limit-for-an-existing-position)
        - [On the Web Platform](#on-the-web-platform-1)
        - [On the Mobile App](#on-the-mobile-app-1)
    - [Important Notes](#important-notes)
  - [How do I set a stop-loss order for an existing position on HTX?](#how-do-i-set-a-stop-loss-order-for-an-existing-position-on-htx-)
    - [On the Web Platform](#on-the-web-platform-2)
    - [On the Mobile App](#on-the-mobile-app-2)
    - [Key Notes](#key-notes)
  - [Can I adjust the stop-loss price after it's set on HTX?](#can-i-adjust-the-stop-loss-price-after-it-s-set-on-htx-)
    - [On the Web Platform](#on-the-web-platform-3)
    - [On the Mobile App](#on-the-mobile-app-3)
    - [Key Notes](#key-notes-1)
  - [Can I adjust a stop-loss order based on market conditions on HTX?](#can-i-adjust-a-stop-loss-order-based-on-market-conditions-on-htx-)
    - [Adjusting Stop-Loss on HTX (Web & Mobile)](#adjusting-stop-loss-on-htx--web---mobile-)
      - [For Web Users](#for-web-users)
      - [For Mobile App Users](#for-mobile-app-users)
    - [Key Considerations](#key-considerations)
    - [Strategic Adjustments](#strategic-adjustments)
  - [How do I set a stop-loss order for a specific percentage below my entry price on HTX?](#how-do-i-set-a-stop-loss-order-for-a-specific-percentage-below-my-entry-price-on-htx-)
    - [Setting a Percentage-Based Stop-Loss on HTX](#setting-a-percentage-based-stop-loss-on-htx)
      - [For Existing Positions (Web & Mobile)](#for-existing-positions--web---mobile-)
      - [Key Notes](#key-notes-2)
      - [Example Scenario](#example-scenario)
  - [Can I set a stop-loss order and a take-profit order simultaneously on HTX?](#can-i-set-a-stop-loss-order-and-a-take-profit-order-simultaneously-on-htx-)
    - [Setting Both Orders Together on HTX](#setting-both-orders-together-on-htx)
      - [Method 1: When Opening a Position](#method-1--when-opening-a-position)
      - [Method 2: For Existing Positions](#method-2--for-existing-positions)
    - [Key Rules](#key-rules)
    - [Notes](#notes)
    - [Example Scenario](#example-scenario-1)
  - [Are there any fees associated with setting stop-loss and take-profit orders on HTX?](#are-there-any-fees-associated-with-setting-stop-loss-and-take-profit-orders-on-htx-)
    - [Key Details](#key-details)
  - [Can I set multiple stop-loss and take-profit orders for a single position on HTX?](#can-i-set-multiple-stop-loss-and-take-profit-orders-for-a-single-position-on-htx-)
    - [Key Features of HTX's Stop-Loss/Take-Profit System](#key-features-of-htx-s-stop-loss-take-profit-system)
    - [How to Set Multiple Orders](#how-to-set-multiple-orders)
      - [For New Positions (Web/Mobile)](#for-new-positions--web-mobile-)
      - [For Existing Positions](#for-existing-positions)
    - [Important Notes](#important-notes-1)
    - [Example Scenario](#example-scenario-2)
  - [How do I prioritize multiple stop-loss and take-profit orders on HTX?](#how-do-i-prioritize-multiple-stop-loss-and-take-profit-orders-on-htx-)
    - [HTX Order Priority System](#htx-order-priority-system)
    - [How to Set Multiple Orders](#how-to-set-multiple-orders-1)
      - [For New Positions](#for-new-positions)
      - [For Existing Positions](#for-existing-positions-1)
    - [Key Limitations](#key-limitations)
    - [Strategy for Multiple Take-Profit Levels](#strategy-for-multiple-take-profit-levels)
    - [Example Scenario](#example-scenario-3)
  - [Can I set a hierarchy for my stop-loss and take-profit orders on HTX?](#can-i-set-a-hierarchy-for-my-stop-loss-and-take-profit-orders-on-htx-)
    - [Key Rules for Multiple Orders on HTX](#key-rules-for-multiple-orders-on-htx)
    - [Practical Execution Example](#practical-execution-example)
    - [Advanced Management Tips](#advanced-management-tips)
  - [Are there any tools or features on HTX that help manage multiple stop-loss and take-profit orders?](#are-there-any-tools-or-features-on-htx-that-help-manage-multiple-stop-loss-and-take-profit-orders-)
    - [HTX's Native Features for Managing Multiple Orders](#htx-s-native-features-for-managing-multiple-orders)
    - [Limitations vs. Advanced Tools](#limitations-vs-advanced-tools)
    - [Workarounds & Third-Party Solutions](#workarounds---third-party-solutions)
    - [Example Workflow on HTX](#example-workflow-on-htx)
  - [Can I automate my stop-loss and take-profit orders on HTX?](#can-i-automate-my-stop-loss-and-take-profit-orders-on-htx-)
    - [Native HTX Features](#native-htx-features)
    - [Limitations of HTX's Native Tools](#limitations-of-htx-s-native-tools)
    - [Workarounds for Advanced Automation](#workarounds-for-advanced-automation)
    - [Key Takeaways](#key-takeaways)
  - [What is the cooldown feature for stop-loss orders on HTX?](#what-is-the-cooldown-feature-for-stop-loss-orders-on-htx-)
    - [HTX's Native Stop-Loss Functionality](#htx-s-native-stop-loss-functionality)
    - [Workarounds for Cooldown-Like Functionality](#workarounds-for-cooldown-like-functionality)
    - [Example: How Altrady's Cooldown Works (vs. HTX)](#example--how-altrady-s-cooldown-works--vs-htx-)
    - [Key Takeaway](#key-takeaway)
  - [Can I combine a cooldown with an emergency stop-loss on HTX?](#can-i-combine-a-cooldown-with-an-emergency-stop-loss-on-htx-)
    - [HTX's Native Stop-Loss Limitations](#htx-s-native-stop-loss-limitations)
    - [Altrady's Advanced Features (Third-Party Solution)](#altrady-s-advanced-features--third-party-solution-)
      - [1. Stop-Loss Cooldown](#1-stop-loss-cooldown)
      - [2. Emergency Stop-Loss](#2-emergency-stop-loss)
      - [3. Trailing Stop-Loss](#3-trailing-stop-loss)
    - [How to Implement on HTX](#how-to-implement-on-htx)
    - [Key Takeaway](#key-takeaway-1)
  - [What happens if the price reaches the emergency stop-loss during a cooldown?](#what-happens-if-the-price-reaches-the-emergency-stop-loss-during-a-cooldown-)
    - [Key Mechanism](#key-mechanism)
    - [Example Scenario](#example-scenario-4)
    - [HTX Limitation vs. Altrady's Solution](#htx-limitation-vs-altrady-s-solution)
      - [Why This Matters](#why-this-matters)

## How to set a stop-loss limit order on the Huobi HTX crypto exchange

Here are detailed instructions on how to set a stop-loss limit order on the Huobi HTX crypto exchange. The process is similar whether you are using the web platform or the mobile app.

### What is a Stop-Loss Limit Order?

A stop-loss limit order is a type of order that helps you manage risk by automatically closing a position when the market price reaches a specified trigger price. Once triggered, the system places a limit order at your pre-set price.

### Steps to Set a Stop-Loss Limit Order

#### 1. Setting a Stop-Loss Limit When Opening a Position

You can set a stop-loss limit while creating a new position:

##### On the Web Platform

1. Log in to your HTX account and navigate to the trading page.
2. Choose the trading pair (e.g., BTC/USDT) and select "Limit Order" or "Market Order" to open your position.
3. Check the "Stop-Limit" option (or equivalent checkbox for Take-Profit/Stop-Loss).
4. Enter the following details:
   - **Trigger Price:** The price at which the stop-loss order will activate.
   - **Order Price:** The price at which you want to sell/buy once triggered.
   - **Amount:** The quantity of the asset you want to sell/buy.
5. Click "Open Long" (for buying) or "Open Short" (for selling) to confirm your position with the stop-loss strategy.

##### On the Mobile App

1. Open the HTX app and log in.
2. Select your trading pair and navigate to the "Limit Order" or "Market Order" section.
3. Tap on "Stop-Limit" or "Take-Profit/Stop-Loss."
4. Input:
   - Trigger Price
   - Order Price
   - Amount
5. Confirm by clicking "Open Long" or "Open Short."

#### 2. Setting a Stop-Loss Limit for an Existing Position

If you already hold an open position, you can add a stop-loss limit as follows:

##### On the Web Platform

1. Go to your active positions under the "Positions" tab.
2. Locate the position for which you want to set a stop-loss.
3. Click on "Stop-Limit" or "Take-Profit/Stop-Loss."
4. Enter:
   - **Trigger Price:** The price that triggers the stop-loss.
   - **Order Price:** The price at which you want to close your position after triggering.
   - **Amount:** The quantity of contracts/assets to close.
5. Confirm your settings.

##### On the Mobile App

1. Navigate to your active positions under "Positions."
2. Select the specific position and tap on "Stop-Limit" or "Take-Profit/Stop-Loss."
3. Input:
   - Trigger Price
   - Order Price
   - Amount
4. Save and confirm.

### Important Notes

- For long positions, ensure that your stop-loss price is lower than both your entry price and current market price.
- For short positions, ensure that your stop-loss price is higher than both your entry price and current market price.
- Once triggered, if market conditions change rapidly, there is no guarantee that your limit order will be filled at exactly the specified price.
- You can check all active stop-loss orders under [Open Orders] > [Stop-Limit] on both web and app platforms.

By following these steps, you can effectively manage risk while trading on HTX!

## How do I set a stop-loss order for an existing position on HTX?

To set a stop-loss order for an existing position on the HTX (Huobi) crypto exchange, follow these steps:

### On the Web Platform

1. **Log in to Your Account**:

   - Access your HTX account and go to the trading interface.

2. **Navigate to Positions**:

   - Locate your active positions under the "Positions" tab.

3. **Select the Position**:

   - Identify the specific position for which you want to set a stop-loss order.

4. **Open Stop-Limit Settings**:

   - Click on the "Stop-Limit" or "Take-Profit/Stop-Loss" option for the selected position.

5. **Input Stop-Loss Details**:

   - **Trigger Price**: The price at which the stop-loss order will activate.
   - **Order Price**: The price at which you want to close your position after triggering.
   - **Amount**: The quantity of assets/contracts to sell or close.

6. **Confirm the Order**:

   - Review your inputs and click "Confirm" or "Set Order." The system will now monitor the market and execute your stop-loss order when the trigger price is reached.

7. **Check Active Orders**:
   - You can view and manage your stop-loss order under [Open Orders] > [Stop-Limit].

### On the Mobile App

1. **Log in and Open Positions**:

   - Launch the HTX app, log in, and go to the "Positions" section.

2. **Select a Position**:

   - Tap on the position you wish to manage.

3. **Set Stop-Loss**:

   - Tap on "Take-Profit/Stop-Loss" or "Stop-Limit."
   - Enter:
     - **Trigger Price**
     - **Order Price**
     - **Amount**

4. **Save and Confirm**:

   - Confirm your settings by tapping "Set Order" or "Close."

5. **Monitor Orders**:
   - Check stop-loss orders under [Open Orders] > [Stop-Limit].

### Key Notes

- For long positions, ensure that the stop-loss price is lower than both your entry price and current market price.
- For short positions, ensure that the stop-loss price is higher than both your entry price and current market price.
- If market conditions change rapidly, there is no guarantee that your limit order will be filled at exactly the specified price.
- You can also set take-profit orders alongside stop-loss orders for comprehensive risk management.

By following these steps, you can effectively manage risk for your existing positions on HTX!

## Can I adjust the stop-loss price after it's set on HTX?

Yes, you can adjust the stop-loss price after it has been set on HTX (Huobi). Here's how you can do it:

### On the Web Platform

1. **Log in to Your Account**:

   - Access your HTX account and navigate to the trading interface.

2. **Go to Open Orders**:

   - Under the "Open Orders" section, locate the stop-loss order you want to adjust. This is typically found under [Open Orders] > [Stop-Limit].

3. **Modify the Stop-Loss Order**:

   - Select the stop-loss order and click on the "Edit" or "Modify" option (if available).
   - Adjust the following details as needed:
     - **Trigger Price**: The price at which the stop-loss will activate.
     - **Order Price**: The price at which the position will close after triggering.
     - **Amount**: The quantity of assets/contracts.

4. **Save Changes**:
   - Confirm your changes by clicking "Update" or "Save." The system will now apply the new stop-loss parameters.

### On the Mobile App

1. **Log in and Navigate to Positions**:

   - Open the HTX app, log in, and go to the "Positions" or "Open Orders" section.

2. **Locate Your Stop-Loss Order**:

   - Find the active stop-loss order you wish to adjust under [Open Orders] > [Stop-Limit].

3. **Edit the Stop-Loss Order**:

   - Tap on the stop-loss order and select "Modify" or "Edit."
   - Update:
     - **Trigger Price**
     - **Order Price**
     - **Amount**

4. **Save Changes**:
   - Confirm your modifications by tapping "Save" or "Update."

### Key Notes

- Adjustments are subject to market conditions, so ensure that your new stop-loss values align with your trading strategy.
- If you cannot directly modify an order, you may need to cancel the existing stop-loss order and create a new one with updated parameters.
- Changes can be monitored in real-time under [Open Orders] > [Stop-Limit].

By following these steps, you can dynamically manage your risk by adjusting stop-loss orders as market conditions evolve.

## Can I adjust a stop-loss order based on market conditions on HTX?

Yes, you can adjust a stop-loss order for an existing position on HTX (formerly Huobi). Here's how to modify it based on market conditions:

### Adjusting Stop-Loss on HTX (Web & Mobile)

#### For Web Users

1. Log in and go to your **Open Positions** under the trading dashboard.
2. Locate your active position and click **"Stop-Limit"** or **"Take-Profit/Stop-Loss."**
3. Modify:
   - **Trigger Price** (new stop-loss activation level)
   - **Order Price** (execution price after triggering)
   - **Amount** (quantity to close)
4. Confirm changes. If HTX doesn't allow direct edits, cancel the existing stop-loss and place a new one.

#### For Mobile App Users

1. Open the HTX app and navigate to **Positions**.
2. Tap the position and select **"Stop-Loss"**.
3. Update:
   - Trigger Price
   - Order Price
   - Amount
4. Save changes.

### Key Considerations

- **Long Positions**: Adjust stop-loss **below** current price to lock in profits during uptrends (e.g., raise it as price climbs).
- **Short Positions**: Adjust stop-loss **above** current price to limit downside.
- **Market Volatility**: HTX may not execute orders if prices gap beyond your limit.
- **Alternative Method**: If direct editing isn't supported, cancel the old stop-loss and set a new one.

### Strategic Adjustments

- **Trend Following**: Gradually tighten stop-loss in uptrends (e.g., move it to 5% below recent highs).
- **Support/Resistance**: Place stops just beyond key technical levels (e.g., below support for longs).

HTX's system automatically invalidates conflicting orders (e.g., take-profit if stop-loss triggers first). Always review open orders under **[Stop-Limit]** after adjustments.

## How do I set a stop-loss order for a specific percentage below my entry price on HTX?

Here's how to set a percentage-based stop-loss order on HTX (Huobi):

### Setting a Percentage-Based Stop-Loss on HTX

#### For Existing Positions (Web & Mobile)

1. **Navigate to your open positions**:

   - On **Web**: Go to "Positions" under the trading dashboard.
   - On **Mobile App**: Open the app and tap "Positions."

2. **Select your position**:

   - Choose the asset you want to protect with a stop-loss.

3. **Set Stop-Loss by Percentage (Method 2 - PnL Ratio)**:

   - HTX allows setting stop-loss based on **profit/loss ratio** rather than a fixed price.
   - Input:
     - **Trigger Price/PnL Ratio**: Enter a negative percentage (e.g., `-10%` for a 10% loss threshold).
     - **Order Price**: Auto-fills based on the percentage, but ensure it's executable.
     - **Amount**: Specify the quantity to sell.

4. **Confirm the order**:
   - Click "Set Order" (Web) or tap "Confirm" (Mobile).

#### Key Notes

- **Long Positions**: Stop-loss percentage must be **below** your entry price (e.g., `-5%` to limit downside).
- **Trailing Stop Option**: HTX does not natively support trailing stops, so manual adjustments are required.
- **Execution Risk**: If the market gaps below your stop-loss price, execution may occur at a worse rate.

#### Example Scenario

- Entry Price: **$20,000 (BTC)**
- Desired Stop-Loss: **10% below entry ($18,000)**
- Set **Trigger Price** at `$18,000` (or `-10%` PnL ratio if available).
- Once triggered, HTX places a limit order at your specified price.

For dynamic adjustments, cancel and reset the stop-loss as market conditions change.

## Can I set a stop-loss order and a take-profit order simultaneously on HTX?

Yes, HTX (formerly Huobi) allows you to set both a stop-loss and take-profit order simultaneously for the same position. Here's how to do it:

### Setting Both Orders Together on HTX

#### Method 1: When Opening a Position

1. **Select your trading pair** (e.g., BTC/USDT) and choose **"Limit Order."**
2. **Enable "Stop-Limit"** or "Take-Profit/Stop-Loss" options.
3. **Configure both orders**:
   - **Take-Profit**:
     - **Trigger Price**: Price where you want to lock in profits (must be _above_ entry for longs, _below_ for shorts).
     - **Order Price**: Execution price after triggering (e.g., limit price).
   - **Stop-Loss**:
     - **Trigger Price**: Price to limit losses (must be _below_ entry for longs, _above_ for shorts).
     - **Order Price**: Execution price after triggering.
4. **Confirm** by clicking **"Open Long"** or **"Open Short."**

#### Method 2: For Existing Positions

1. Navigate to **"Positions"** and select your active trade.
2. Click **"Take-Profit/Stop-Loss"** or **"Stop-Limit."**
3. Input both orders:
   - **Take-Profit**: Set trigger and execution prices.
   - **Stop-Loss**: Define your risk threshold.
4. **Save changes**.

### Key Rules

- **Long Positions**:
  - Take-profit price must be **higher** than entry.
  - Stop-loss price must be **lower** than entry.
- **Short Positions**:
  - Take-profit price must be **lower** than entry.
  - Stop-loss price must be **higher** than entry.
- **Order Limits**: Up to 30 active take-profit/stop-loss orders per contract.

### Notes

- HTX executes these as **limit orders**, not OCO (One-Cancels-the-Other). If one triggers, the other remains active until canceled manually.
- Monitor orders under **[Open Orders] > [Stop-Limit]**.

For visual guidance, refer to HTX's [official guide](https://www.htx.com/support/900004783283).

### Example Scenario

- **Entry Price**: $20,000 (BTC long)
- **Take-Profit**: Trigger at $22,000, limit at $21,800.
- **Stop-Loss**: Trigger at $18,500, limit at $18,300.

Both orders can coexist and execute independently based on market conditions.

## Are there any fees associated with setting stop-loss and take-profit orders on HTX?

No, HTX does not charge additional fees for setting stop-loss and take-profit orders. However, standard trading fees apply when these orders are executed.

### Key Details

- **No Setup Fees**: You can place and manage stop-loss/take-profit orders without extra charges.
- **Execution Fees**: Regular trading fees (maker/taker) are applied when the orders trigger and execute.
- **Order Limits**: Up to 30 active stop-loss/take-profit orders per contract are allowed.

For transparency, review HTX's fee structure under their official trading rules.

## Can I set multiple stop-loss and take-profit orders for a single position on HTX?

Yes, you can set both stop-loss and take-profit orders simultaneously for a single position on HTX (formerly Huobi), but there are important limitations and behaviors to understand:

### Key Features of HTX's Stop-Loss/Take-Profit System

1. **Simultaneous Orders**

   - You can set **both** a stop-loss and take-profit order for the same position at the same time, either when opening the position or afterward.
   - Example: For a BTC long position, you could set:
     - Take-profit at **$25,000** (executes if price rises).
     - Stop-loss at **$16,000** (executes if price falls).

2. **Execution Rules**

   - **Not OCO (One-Cancels-the-Other)**: If one order triggers, the other **remains active** unless manually canceled.
   - Example: If your stop-loss executes, the take-profit order stays open until the price reaches its trigger or you cancel it.

3. **Order Limits**
   - Maximum **30 active stop-loss/take-profit orders** per contract.

### How to Set Multiple Orders

#### For New Positions (Web/Mobile)

1. Place a limit/market order and enable **"Stop-Limit"** or **"Take-Profit/Stop-Loss"**.
2. Configure:
   - **Take-Profit**: Trigger + execution price (e.g., +10% from entry).
   - **Stop-Loss**: Trigger + execution price (e.g., -5% from entry).
3. Confirm with **"Open Long/Short"**.

#### For Existing Positions

1. Go to **"Positions"**, select the trade, and click **"Take-Profit/Stop-Loss"**.
2. Set both orders independently (by price or profit rate).

### Important Notes

- **Long Positions**:
  - Take-profit must be **above** entry; stop-loss must be **below**.
- **Short Positions**:
  - Take-profit must be **below** entry; stop-loss must be **above**.
- **No Trailing Stops**: HTX doesn't natively support trailing stops; adjustments must be manual.
- **Partial Triggers**: If the position is partially closed, orders adjust proportionally.

### Example Scenario

- **BTC Long Entry**: $20,000
  - Take-profit: Trigger at **$22,000**, limit at **$21,800**.
  - Stop-loss: Trigger at **$18,000**, limit at **$17,800**.
- If price drops to $18,000, the stop-loss executes, but the take-profit order remains active until canceled or triggered.

For advanced strategies (e.g., scaling out with multiple take-profits), you'll need to place separate orders manually. HTX's system is flexible but requires active management.

Refer to HTX's [official guide](https://www.htx.com/support/900004783283) for updates.

## How do I prioritize multiple stop-loss and take-profit orders on HTX?

Here's how to manage multiple stop-loss and take-profit orders on HTX, along with priority rules:

### HTX Order Priority System

1. **Single Position, Multiple Orders**

   - You can set **both a stop-loss and take-profit simultaneously** for one position, but they operate independently (not OCO).
   - If one triggers, the other **remains active** unless manually canceled.

2. **Partial Execution Handling**

   - If a position is partially closed, orders adjust proportionally.
   - Example: Closing 50% of a BTC long cancels 50% of attached stop-loss/take-profit orders.

3. **Auto-Cancellation Rules**
   - If your position is fully closed, all related orders are **automatically invalidated**.
   - If the stop-loss triggers, the take-profit order is canceled (and vice versa).

### How to Set Multiple Orders

#### For New Positions

1. On the order panel, enable **"Stop-Limit"** or **"Take-Profit/Stop-Loss."**
2. Configure:
   - **Take-Profit**: Trigger + execution price (e.g., +10%).
   - **Stop-Loss**: Trigger + execution price (e.g., -5%).
3. Confirm with **"Open Long/Short"**.

#### For Existing Positions

1. Go to **"Positions"**, select the trade, and click **"Take-Profit/Stop-Loss."**
2. Add/modify orders:
   - **Price-Based**: Directly input trigger/execution prices.
   - **Percentage-Based**: Use PnL ratio (e.g., -5% for stop-loss, +10% for take-profit).

### Key Limitations

- **No Native Trailing Stops**: Adjustments must be manual.
- **Order Cap**: Max **30 active stop-loss/take-profit orders** per contract.
- **Price Rules**:
  - **Longs**: Take-profit > entry price; stop-loss entry price.

### Strategy for Multiple Take-Profit Levels

HTX doesn't support scaling out with automated tiers (e.g., 15%/20% take-profits). Instead:

1. **Manual Approach**: Place separate limit orders at different profit levels.
2. **Post-Execution**: After the first take-profit triggers, adjust the remaining position's stop-loss to lock in profits.

For real-time monitoring, check orders under **[Open Orders] > [Stop-Limit]**.

### Example Scenario

- **BTC Long Entry**: $20,000
  - **Take-Profit 1**: $22,000 (limit at $21,800).
  - **Take-Profit 2**: $24,000 (additional manual order).
  - **Stop-Loss**: $18,000 (limit at $17,800).
- If price hits $22,000, the first take-profit executes, but the stop-loss and second take-profit remain active until canceled or triggered.

Refer to HTX's [official guide](https://www.htx.com/support/900004783283) for updates.

## Can I set a hierarchy for my stop-loss and take-profit orders on HTX?

HTX (formerly Huobi) allows simultaneous setting of stop-loss and take-profit orders, but with specific execution rules rather than a traditional hierarchy system. Here's how order priority and execution work:

### Key Rules for Multiple Orders on HTX

1. **Independent Execution**

   - Stop-loss and take-profit orders operate separately (not as OCO - One Cancels Other)
   - When one triggers, the other remains active until either:
     - The position is fully closed
     - The remaining order triggers
     - You manually cancel it

2. **Auto-Invalidation Rules**

   - If your **position is fully closed**, all attached orders are automatically canceled
   - If a **stop-loss executes**, the take-profit becomes invalid (and vice versa)
   - Partial fills proportionally reduce attached orders

3. **Price Priority Logic**
   - For **long positions**:
     - Take-profit must be set **above** current price
     - Stop-loss must be set **below** current price
   - For **short positions**:
     - Take-profit must be set **below** current price
     - Stop-loss must be set **above** current price

### Practical Execution Example

- **Scenario**: BTC long at $20,000 with:
  - Take-profit at $22,000
  - Stop-loss at $18,000
- **If price drops to $18,000**:
  - Stop-loss triggers
  - Take-profit is automatically invalidated
- **If price rises to $22,000**:
  - Take-profit executes
  - Stop-loss is canceled

### Advanced Management Tips

1. **For Multiple Take-Profit Levels**
   - HTX doesn't support automated scaling - set separate limit orders manually
2. **Order Limits**
   - Max 30 active stop-loss/take-profit orders per contract
3. **Monitoring**
   - Track all active orders under:  
     _Web_: [Open Orders] → [Stop-Limit]  
     _Mobile_: [Orders] → [Stop-Limit]

Unlike platforms with OCO functionality, HTX requires manual adjustment of remaining orders after partial executions. The system prioritizes price-based triggers over order sequence.

## Are there any tools or features on HTX that help manage multiple stop-loss and take-profit orders?

Yes, HTX provides tools to manage multiple stop-loss and take-profit orders, though with some limitations compared to advanced third-party platforms. Here's what you need to know:

### HTX's Native Features for Managing Multiple Orders

1. **Simultaneous Stop-Loss & Take-Profit**

   - You can set **both** a stop-loss and take-profit for the same position at once.
   - These orders are **interlinked**: If one triggers, the other is automatically canceled.

2. **Order Limits**

   - Max **30 active stop-loss/take-profit orders** per contract.

3. **Partial Execution Handling**

   - If your position is partially closed, orders adjust proportionally.

4. **Price/Rate-Based Triggers**

   - Set orders by:
     - **Fixed price** (e.g., stop-loss at $18,000, take-profit at $22,000).
     - **Profit/loss ratio** (e.g., -5% stop-loss, +10% take-profit).

5. **Monitoring & Adjustment**
   - Track active orders under **[Open Orders] → [Stop-Limit]**.
   - Modify or cancel orders anytime before execution.

### Limitations vs. Advanced Tools

- **No Trailing Stops**: HTX lacks native trailing stop-loss/take-profit.
- **No Multi-Tier Take-Profit**: Cannot auto-scale out at multiple price levels (requires manual orders).
- **No OCO (One-Cancels-Other)**: While linked, orders don't fully replicate OCO logic.

### Workarounds & Third-Party Solutions

For advanced features like **trailing stops, multi-target take-profits, or stop-loss cooldowns**, consider:

- **Trading Bots**: Platforms like 3Commas or Bitsgap integrate with HTX for:
  - Dynamic trailing stops.
  - Multi-level profit-taking.
  - Risk calculators.
- **APIs**: Customize automated strategies via HTX's API.

### Example Workflow on HTX

1. **Open a BTC long at $20,000**.
2. Set:
   - Take-profit: $22,000 (limit at $21,800).
   - Stop-loss: $18,000 (limit at $17,800).
3. If price hits $18,000:
   - Stop-loss executes, take-profit cancels automatically.

For complex strategies, third-party tools are recommended. HTX's native system prioritizes simplicity over granular control.

Refer to HTX's [official guide](https://www.htx.com/support/900004783283) for updates.

## Can I automate my stop-loss and take-profit orders on HTX?

HTX provides built-in functionality for setting stop-loss and take-profit orders, but offers limited automation features for advanced management. Here's a breakdown of the available tools:

### Native HTX Features

1. **Simultaneous Order Placement**

   - You can set **both stop-loss and take-profit** when opening a position or for existing positions.
   - These orders are **interlinked**: If one triggers, the other is automatically canceled.

2. **Trigger Methods**

   - **Price-Based**: Set exact trigger/execution prices (e.g., stop-loss at $18,000, take-profit at $22,000).
   - **Profit Rate**: Define triggers as percentages (e.g., +10% take-profit, -5% stop-loss).

3. **Order Limits**

   - Max **30 active stop-loss/take-profit orders** per contract.

4. **Partial Execution**
   - Orders adjust proportionally if the position is partially closed.

### Limitations of HTX's Native Tools

- **No Trailing Stops**: Cannot automatically adjust stop-loss/take-profit levels as prices move.
- **No Multi-Tier Take-Profit**: Requires manual orders for scaling out at multiple price levels.
- **No OCO (One-Cancels-Other)**: While linked, orders don't fully replicate OCO logic.

### Workarounds for Advanced Automation

1. **Third-Party Tools**

   - Platforms like **3Commas** integrate with HTX to offer:
     - Trailing stop-loss/take-profit.
     - Multi-level profit-taking strategies.
     - Customizable risk management via APIs.

2. **HTX API**
   - Build custom scripts to automate order adjustments based on market conditions.

### Key Takeaways

- **Basic Automation**: HTX supports simultaneous stop-loss/take-profit orders with auto-cancellation.
- **Advanced Needs**: Use third-party tools or APIs for trailing stops, multi-target exits, or dynamic adjustments.

For details, refer to HTX's [official guide](https://www.htx.com/support/900004783283).

## What is the cooldown feature for stop-loss orders on HTX?

HTX (formerly Huobi) does not offer a native cooldown feature for stop-loss orders like some third-party trading platforms (e.g., Altrady). Here's a clear breakdown of what HTX provides and alternative solutions:

### HTX's Native Stop-Loss Functionality

1. **Basic Stop-Limit Orders**

   - HTX allows standard stop-loss orders (triggered at a set price) but **lacks cooldown timers or emergency stop-loss tiers**.
   - Orders execute immediately when the trigger price is hit, with no delay or recovery window.

2. **Linked Take-Profit/Stop-Loss**

   - You can set both orders simultaneously, but they operate independently (not OCO).
   - Partial fills adjust remaining orders proportionally.

3. **Limitations**
   - No native support for:
     - **Cooldown periods** (delayed execution after trigger).
     - **Emergency stop-loss** (secondary fallback price).
     - **Candle-close confirmation** (waiting for a candle to close below the stop price).

### Workarounds for Cooldown-Like Functionality

1. **Manual Adjustment**

   - Monitor positions and **manually reset stop-losses** if prices recover after a dip (requires active trading).

2. **Third-Party Tools**

   - Platforms like **Altrady** or **3Commas** integrate with HTX to add advanced features:
     - **Time-based cooldowns** (e.g., 5-minute delay before executing).
     - **Candle-close confirmation** (only trigger if a 15m/1H candle closes below the stop price).
     - **Emergency stop-loss** (bypass cooldown if prices crash further).

3. **HTX API**
   - Developers can build custom scripts to simulate cooldowns or multi-tier stops.

### Example: How Altrady's Cooldown Works (vs. HTX)

| Feature              | HTX Native | Altrady Integration |
| -------------------- | ---------- | ------------------- |
| Stop-Loss Cooldown   | ❌ No      | ✅ Yes (1m–30d)     |
| Emergency Stop-Loss  | ❌ No      | ✅ Yes              |
| Candle-Close Trigger | ❌ No      | ✅ Yes              |
| Trailing Stop-Loss   | ❌ No      | ✅ Yes              |

### Key Takeaway

HTX's stop-loss system is straightforward but lacks advanced risk-management features like cooldowns. For automated recovery windows or multi-tier protection, use third-party tools connected via API.

For HTX's official order types, refer to their [Trading Guide](https://www.htx.com/support/900004783283).

## Can I combine a cooldown with an emergency stop-loss on HTX?

HTX (formerly Huobi) **does not** offer native cooldown or emergency stop-loss features for its stop-loss orders. However, third-party tools like **Altrady** can provide these advanced functionalities when connected to HTX via API. Here's a detailed breakdown:

### HTX's Native Stop-Loss Limitations

1. **Basic Stop-Loss Orders**

   - HTX only supports standard **stop-limit** or **stop-market** orders.
   - **No cooldown**: Orders trigger immediately when the stop price is hit.
   - **No emergency stop-loss tiers**: No secondary fallback price protection.

2. **Take-Profit/Stop-Loss Pairing**
   - You can set both simultaneously, but they operate independently (not as OCO).

### Altrady's Advanced Features (Third-Party Solution)

Altrady integrates with HTX to add:

#### 1. Stop-Loss Cooldown

- **Time-Based**: Delays execution for a set duration (e.g., 10 minutes) to allow price recovery.
  - Example: If BTC drops to $18,000 (stop price), the cooldown timer starts. If price recovers above $18,000 before the timer ends, the order cancels.
- **Candle-Close**: Waits for a candle (e.g., 15m) to close below the stop price before triggering.

#### 2. Emergency Stop-Loss

- Activates **immediately** if price crashes further during cooldown.
  - Example: If BTC falls to $16,000 (emergency price) during a 10-minute cooldown, it sells instantly.

#### 3. Trailing Stop-Loss

- Adjusts stop price as the asset moves favorably (HTX lacks this natively).

### How to Implement on HTX

1. **Connect Altrady to HTX** via API.
2. **Set Up Smart Orders**:
   - Configure cooldown duration (time or candle-based).
   - Define emergency stop-loss price (must be worse than main stop).
3. **Monitor**: Altrady manages executions, canceling orders if prices recover.

### Key Takeaway

To combine cooldown and emergency stop-loss on HTX:

- Use **Altrady** or similar third-party tools for advanced automation.
- HTX's native system is limited to basic stop-loss/take-profit orders.

For HTX's official order types, see their [Trading Guide](https://www.htx.com/support/900004783283). For Altrady's cooldown setup, refer to their [documentation](https://support.altrady.com/en/article/smart-orders-stop-loss-including-optional-cooldowns-time-and-candle-close-new-1hqv471/).

## What happens if the price reaches the emergency stop-loss during a cooldown?

Here's how **cooldown + emergency stop-loss** works on platforms like Altrady (which integrates with HTX via API):

### Key Mechanism

1. **Cooldown Activation**

   - When price hits your **main stop-loss**, a timer starts (e.g., 10 minutes).
   - If price recovers **above the stop-loss** before the timer ends, the order cancels.

2. **Emergency Stop-Loss (ESL) Override**
   - During cooldown, if price crashes further to your **ESL price**, it:
     - **Bypasses the cooldown**.
     - Executes a **market order immediately** to close the position.
   - ESL must be worse than the main stop (e.g., for longs: ESL ℹ️ Source: [Altrady's Stop-Loss Documentation](https://support.altrady.com/en/article/smart-orders-stop-loss-including-optional-cooldowns-time-and-candle-close-new-1hqv471/)

### Example Scenario

| Time | Price                                                        | Action                                           |
| ---- | ------------------------------------------------------------ | ------------------------------------------------ |
| 1:00 | $50                                                          | Entry filled                                     |
| 1:05 | $40                                                          | Hits main stop-loss → 10m cooldown starts        |
| 1:08 | $35                                                          | Reaches ESL → sells instantly (ignores cooldown) |
| 1:15 | $42 (If ESL wasn't hit, checks if price recovered above $40) |

### HTX Limitation vs. Altrady's Solution

| Feature | HTX Native | Altrady + HTX API |
| Cooldown Period | ❌ No | ✅ Yes (1m–30d) |
| Emergency Stop-Loss | ❌ No | ✅ Yes |
| Candle-Close Trigger | ❌ No | ✅ Yes |

#### Why This Matters

Cooldown: Prevents panic-selling during brief dips.

Emergency Stop-Loss: Protects against extreme crashes during cooldown.

For HTX users, third-party tools like Altrady are required for this advanced risk management.
