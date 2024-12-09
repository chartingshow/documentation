//@version=5
// POC Value Area
// Updated by ChartingShow to version 5 and correct all the coding errors.
// https://www.tradingview.com/script/dkGe7rmo-Chart-Champions-Part-2-CCV-IBs-POCs/
//
// This indicator is a Market Profiling tool used to analyse the Point of Control 
// (POC) and Value Area (VAH/VAL) on the daily, weekly and monthly timeframes. 
// It also optionally displays historical Value Areas to help find confluence
// using past data.
//
// The Value Area is a range of prices where the majority of trading volume took 
// place on the prior trading day. In specific, this area is the range where 70% 
// of the prior day’s volume happened. The value area is approximately one 
// standard deviation above and below the average highest volume price. With
// this knowledge, there are specific probabilities of market behavior we can 
// understand to digest the value area. The value area gives us an idea of where 
// the smart money is playing ball and where the institutions are guiding the 
// market. From this data, we can derive intra-day strategies that capitalize 
// on market behavior.
//
indicator(title='POC Value Area POC-VAH-VAL v5', shorttitle='POC Value Area', overlay=true)

ShowLabelBackground = input(false, title='Show label background')
ShowLabelValues = input(false, title='Show label values')
ExtendAxisLine = input(false, title='Extend axis lines across chart')
MaxLookbackDays = input.int(64, 'Maximum lookback days', minval=0, group='CCV Settings')
VAPercent = input.float(0.68, 'Value Area (Igor 0.7 / Daniel 0.68)', minval=0.1, maxval=1, step=0.1)
CCVResolution = input.float(1, title='Resolution (Change resolution to Symbol decimal)', tooltip='E.g. BTCUSD = 1, XRPUSD = 0.00001, QTUMUSD = 0.001')

CCVDailyShowDev = input.bool(true, title='Show developing day', group='CCV Daily')
CCVDailyShowPrev = input.bool(true, title='Show previous day', group='CCV Daily')
CCVDailyShowArea = input.bool(true, title='Show daily areas', group='CCV Daily')
CCVDailyColor = input.color(color.yellow, title='Daily color', group='CCV Daily', inline='Input 0')
CCVDailyTextColor = input.color(color.black, title='Daily text color', group='CCV Daily', inline='Input 0')

CCVWeeklyShowDev = input.bool(true, title='Show developing week', group='CCV Weekly')
CCVWeeklyShowPrev = input.bool(true, title='Show previous week', group='CCV Weekly')
CCVWeeklyShowArea = input.bool(true, title='Show weekly areas', group='CCV Weekly')
CCVWeeklyColor = input.color(color.blue, title='Weekly color', group='CCV Weekly', inline='Input 0')
CCVWeeklyTextColor = input.color(color.white, title='Weekly text color', group='CCV Weekly', inline='Input 0')

CCVMonthlyShowDev = input.bool(true, title='Show developing month', group='CCV Monthly')
CCVMonthlyShowPrev = input.bool(true, title='Show previous month', group='CCV Monthly')
CCVMonthlyShowArea = input.bool(true, title='Show monthly areas', group='CCV Monthly')
CCVMonthlyColor = input.color(color.purple, title='Monthly color', group='CCV Monthly', inline='Input 0')
CCVMonthlyTextColor = input.color(color.white, title='Monthly text color', group='CCV Monthly', inline='Input 0')

// Generic
ExtendOption = ExtendAxisLine ? extend.both : extend.right
ShowLabelBackgroundOption = ShowLabelBackground ? label.style_label_left : label.style_none
LabelWhitespace = ShowLabelBackground ? '' : '                           '
MaxLookbackMs = 1000 * 60 * 60 * 24 * MaxLookbackDays
LookbackWindow = MaxLookbackMs == 0 or time > timenow - MaxLookbackMs

// Functions
is_new_bar(t) =>
    ta.change(time(t)) != 0

round_to_nearest(v, x) =>
    math.round(v / x) * x

f_poc(tf) =>
    var a = array.new_float(0)

    tick_size = math.max(syminfo.mintick, CCVResolution)
    a_min = 0.0
    a_min := nz(a_min[1], round_to_nearest(low, tick_size))
    a_max = 0.0
    a_max := nz(a_max[1], round_to_nearest(high, tick_size))

    d_switch = is_new_bar(tf)

    if LookbackWindow
        if d_switch
            a_min := low
            a_max := high
            array.clear(a)

        // Scaled min max
        v_min = int(round_to_nearest(low - a_min, tick_size) / tick_size)
        v_max = int(round_to_nearest(high - a_min, tick_size) / tick_size)

        // Scaled candle range
        ticks = v_max - v_min
        vol = volume / (ticks == 0 ? 1 : ticks)
        for i = v_min to math.max(v_max - 1, v_min) by 1

            // Insert new low value
            if i < 0
                array.insert(a, i - v_min, vol)
                continue

            // Adjust index
            offset = v_min < 0 ? math.abs(v_min) : 0
            index = int(i + offset)

            // Push new high value
            if index >= array.size(a)
                array.push(a, vol)
                continue

            // Update existing value
            v = array.get(a, index)
            array.set(a, index, v + vol)

        // Array bounds
        a_min := math.min(a_min, round_to_nearest(low, tick_size))
        a_max := math.max(a_max, round_to_nearest(high, tick_size))
        a_size = array.size(a)

        // { POC

        poc_index = -1
        poc_prev = -1.0
        sum_vol = 0.0

        for i = 0 to a_size - 1 by 1
            poc_current = array.get(a, i)
            sum_vol += poc_current

            if poc_current > poc_prev
                poc_prev := poc_current
                poc_index := i
                poc_index

        // }

        // { VA

        va_high_index = poc_index
        va_low_index = poc_index

        va_vol_cap = sum_vol * VAPercent
        sum_va_vol = array.get(a, poc_index)

        for i = 1 to a_size - 1 by 1
            above = 0.0
            if va_high_index + 1 < a_size - 1
                above += nz(array.get(a, va_high_index + 1), 0.0)
                above
            if va_high_index + 2 < a_size - 1
                above += nz(array.get(a, va_high_index + 2), 0.0)
                above

            below = 0.0
            if va_low_index - 1 > 0
                below += nz(array.get(a, va_low_index - 1), 0.0)
                below
            if va_low_index - 2 > 0
                below += nz(array.get(a, va_low_index - 2), 0.0)
                below

            if above > below
                va_high_index := math.min(va_high_index + 2, a_size - 1)
                sum_va_vol += above
                sum_va_vol
            else
                va_low_index := math.max(va_low_index - 2, 0)
                sum_va_vol += below
                sum_va_vol

            if sum_va_vol >= va_vol_cap or va_low_index <= 0 and va_high_index >= a_size - 1
                break

        // }

        float poc = poc_index * tick_size + a_min
        float va_high = va_high_index * tick_size + a_min
        float va_low = va_low_index * tick_size + a_min
        float pd_poc = 0.0
        float prev_va_high = 0.0
        float prev_va_low = 0.0
        float prev_pd_poc = 0.0

        if d_switch
            pd_poc := poc[1]
            prev_va_high := va_high[1]
            prev_va_low := va_low[1]
            prev_pd_poc := poc[1]
            prev_pd_poc
        else
            pd_poc := pd_poc[1]
            prev_va_high := prev_va_high[1]
            prev_va_low := prev_va_low[1]
            prev_pd_poc := prev_pd_poc[1]
            prev_pd_poc

        [poc, va_high, va_low, pd_poc, prev_va_high, prev_va_low, prev_pd_poc]
    else
        [na, na, na, na, na, na, na]

f_poc_label(txt, val) =>
    if ShowLabelValues
        LabelWhitespace + txt + ' - ' + str.tostring(val)
    else
        LabelWhitespace + txt

// Daily CCV
[d_poc, d_vah, d_val, pd_poc, pd_vah, pd_val, dbl_poc] = f_poc('D')

d_open = request.security(syminfo.tickerid, 'D', open, lookahead=barmerge.lookahead_off)

pd_poc_plot = plot(CCVDailyShowArea ? pd_poc : na, 'pdPOC', bool(ta.change(pd_poc)) ? na : color.new(CCVDailyColor, 60))
pd_vah_plot = plot(CCVDailyShowArea ? pd_vah : na, 'pdVAH', bool(ta.change(pd_vah)) ? na : color.new(CCVDailyColor, 60))
pd_val_plot = plot(CCVDailyShowArea ? pd_val : na, 'pdVAL', bool(ta.change(pd_val)) ? na : color.new(CCVDailyColor, 60))
fill(pd_vah_plot, pd_val_plot, CCVDailyShowArea ? color.new(CCVDailyColor, 90) : na)

line d_open_line = line.new(CCVDailyShowDev ? bar_index[1] : na, d_open, bar_index, d_open, color=CCVDailyColor, style=line.style_dashed, width=1, extend=ExtendOption)
line d_poc_line = line.new(CCVDailyShowDev ? bar_index[1] : na, d_poc, bar_index, d_poc, color=CCVDailyColor, style=line.style_dashed, width=1, extend=ExtendOption)
line pd_poc_line = line.new(CCVDailyShowPrev ? bar_index[1] : na, pd_poc, bar_index, pd_poc, color=CCVDailyColor, style=line.style_dashed, width=1, extend=ExtendOption)
line pd_vah_line = line.new(CCVDailyShowPrev ? bar_index[1] : na, pd_vah, bar_index, pd_vah, color=CCVDailyColor, style=line.style_dashed, width=1, extend=ExtendOption)
line pd_val_line = line.new(CCVDailyShowPrev ? bar_index[1] : na, pd_val, bar_index, pd_val, color=CCVDailyColor, style=line.style_dashed, width=1, extend=ExtendOption)

line.delete(d_open_line[1])
line.delete(d_poc_line[1])
line.delete(pd_poc_line[1])
line.delete(pd_vah_line[1])
line.delete(pd_val_line[1])

d_open_label = label.new(CCVDailyShowDev ? timenow : na, d_open, xloc=xloc.bar_time, text=f_poc_label('dOpen', d_open), color=color.blue, textcolor=ShowLabelBackground ? CCVDailyTextColor : CCVDailyColor, style=ShowLabelBackgroundOption, size=size.small)
d_poc_label = label.new(CCVDailyShowDev ? timenow : na, d_poc, xloc=xloc.bar_time, text=f_poc_label('dPOC', d_poc), color=CCVDailyColor, textcolor=ShowLabelBackground ? CCVDailyTextColor : CCVDailyColor, style=ShowLabelBackgroundOption, size=size.small)
pd_poc_label = label.new(CCVDailyShowPrev ? timenow : na, pd_poc, xloc=xloc.bar_time, text=f_poc_label('pdPOC', pd_poc), color=CCVDailyColor, textcolor=ShowLabelBackground ? CCVDailyTextColor : CCVDailyColor, style=ShowLabelBackgroundOption, size=size.small)
pd_vah_label = label.new(CCVDailyShowPrev ? timenow : na, pd_vah, xloc=xloc.bar_time, text=f_poc_label('pdVAH', pd_vah), color=CCVDailyColor, textcolor=ShowLabelBackground ? CCVDailyTextColor : CCVDailyColor, style=ShowLabelBackgroundOption, size=size.small)
pd_val_label = label.new(CCVDailyShowPrev ? timenow : na, pd_val, xloc=xloc.bar_time, text=f_poc_label('pdVAL', pd_val), color=CCVDailyColor, textcolor=ShowLabelBackground ? CCVDailyTextColor : CCVDailyColor, style=ShowLabelBackgroundOption, size=size.small)

label.delete(d_open_label[1])
label.delete(d_poc_label[1])
label.delete(pd_poc_label[1])
label.delete(pd_vah_label[1])
label.delete(pd_val_label[1])

// Weekly CCV
[w_poc, w_vah, w_val, pw_poc, pw_vah, pw_val, wbl_poc] = f_poc('W')

w_open = request.security(syminfo.tickerid, 'W', open, lookahead=barmerge.lookahead_off)

pw_poc_plot = plot(CCVWeeklyShowArea ? pw_poc : na, 'pwPOC', bool(ta.change(pw_poc)) ? na : color.new(CCVWeeklyColor, 60))
pw_vah_plot = plot(CCVWeeklyShowArea ? pw_vah : na, 'pwVAH', bool(ta.change(pw_vah)) ? na : color.new(CCVWeeklyColor, 60))
pw_val_plot = plot(CCVWeeklyShowArea ? pw_val : na, 'pwVAL', bool(ta.change(pw_val)) ? na : color.new(CCVWeeklyColor, 60))
fill(pw_vah_plot, pw_val_plot, CCVWeeklyShowArea ? color.new(CCVWeeklyColor, 90) : na)

line w_open_line = line.new(CCVWeeklyShowDev ? bar_index[1] : na, w_open, bar_index, w_open, color=CCVWeeklyColor, style=line.style_dashed, width=1, extend=ExtendOption)
line w_poc_line = line.new(CCVWeeklyShowDev ? bar_index[1] : na, w_poc, bar_index, w_poc, color=CCVWeeklyColor, style=line.style_dashed, width=1, extend=ExtendOption)
line pw_poc_line = line.new(CCVWeeklyShowPrev ? bar_index[1] : na, pw_poc, bar_index, pw_poc, color=CCVWeeklyColor, style=line.style_dashed, width=1, extend=ExtendOption)
line pw_vah_line = line.new(CCVWeeklyShowPrev ? bar_index[1] : na, pw_vah, bar_index, pw_vah, color=CCVWeeklyColor, style=line.style_dashed, width=1, extend=ExtendOption)
line pw_val_line = line.new(CCVWeeklyShowPrev ? bar_index[1] : na, pw_val, bar_index, pw_val, color=CCVWeeklyColor, style=line.style_dashed, width=1, extend=ExtendOption)

line.delete(w_open_line[1])
line.delete(w_poc_line[1])
line.delete(pw_poc_line[1])
line.delete(pw_vah_line[1])
line.delete(pw_val_line[1])

w_open_label = label.new(CCVWeeklyShowDev ? timenow : na, w_open, xloc=xloc.bar_time, text=f_poc_label('wOpen', w_open), color=color.blue, textcolor=ShowLabelBackground ? CCVWeeklyTextColor : CCVWeeklyColor, style=ShowLabelBackgroundOption, size=size.small)
w_poc_label = label.new(CCVWeeklyShowDev ? timenow : na, w_poc, xloc=xloc.bar_time, text=f_poc_label('wPOC', w_poc), color=CCVWeeklyColor, textcolor=ShowLabelBackground ? CCVWeeklyTextColor : CCVWeeklyColor, style=ShowLabelBackgroundOption, size=size.small)
pw_poc_label = label.new(CCVWeeklyShowPrev ? timenow : na, pw_poc, xloc=xloc.bar_time, text=f_poc_label('pwPOC', pw_poc), color=CCVWeeklyColor, textcolor=ShowLabelBackground ? CCVWeeklyTextColor : CCVWeeklyColor, style=ShowLabelBackgroundOption, size=size.small)
pw_vah_label = label.new(CCVWeeklyShowPrev ? timenow : na, pw_vah, xloc=xloc.bar_time, text=f_poc_label('pwVAH', pw_vah), color=CCVWeeklyColor, textcolor=ShowLabelBackground ? CCVWeeklyTextColor : CCVWeeklyColor, style=ShowLabelBackgroundOption, size=size.small)
pw_val_label = label.new(CCVWeeklyShowPrev ? timenow : na, pw_val, xloc=xloc.bar_time, text=f_poc_label('pwVAL', pw_val), color=CCVWeeklyColor, textcolor=ShowLabelBackground ? CCVWeeklyTextColor : CCVWeeklyColor, style=ShowLabelBackgroundOption, size=size.small)

label.delete(w_open_label[1])
label.delete(w_poc_label[1])
label.delete(pw_poc_label[1])
label.delete(pw_vah_label[1])
label.delete(pw_val_label[1])

// Monthly CCV
[m_poc, m_vah, m_val, pm_poc, pm_vah, pm_val, mbl_poc] = f_poc('M')

m_open = request.security(syminfo.tickerid, 'M', open, lookahead=barmerge.lookahead_off)

pm_poc_plot = plot(CCVMonthlyShowArea ? pm_poc : na, 'pmPOC', bool(ta.change(pm_poc)) ? na : color.new(CCVMonthlyColor, 60))
pm_vah_plot = plot(CCVMonthlyShowArea ? pm_vah : na, 'pmVAH', bool(ta.change(pm_vah)) ? na : color.new(CCVMonthlyColor, 60))
pm_val_plot = plot(CCVMonthlyShowArea ? pm_val : na, 'pmVAL', bool(ta.change(pm_val)) ? na : color.new(CCVMonthlyColor, 60))
fill(pm_vah_plot, pm_val_plot, CCVMonthlyShowArea ? color.new(CCVMonthlyColor, 90) : na)

line m_open_line = line.new(CCVMonthlyShowDev ? bar_index[1] : na, m_open, bar_index, m_open, color=CCVMonthlyColor, style=line.style_dashed, width=1, extend=ExtendOption)
line m_poc_line = line.new(CCVMonthlyShowDev ? bar_index[1] : na, m_poc, bar_index, m_poc, color=CCVMonthlyColor, style=line.style_dashed, width=1, extend=ExtendOption)
line pm_poc_line = line.new(CCVMonthlyShowPrev ? bar_index[1] : na, pm_poc, bar_index, pm_poc, color=CCVMonthlyColor, style=line.style_dashed, width=1, extend=ExtendOption)
line pm_vah_line = line.new(CCVMonthlyShowPrev ? bar_index[1] : na, pm_vah, bar_index, pm_vah, color=CCVMonthlyColor, style=line.style_dashed, width=1, extend=ExtendOption)
line pm_val_line = line.new(CCVMonthlyShowPrev ? bar_index[1] : na, pm_val, bar_index, pm_val, color=CCVMonthlyColor, style=line.style_dashed, width=1, extend=ExtendOption)

line.delete(m_open_line[1])
line.delete(m_poc_line[1])
line.delete(pm_poc_line[1])
line.delete(pm_vah_line[1])
line.delete(pm_val_line[1])

m_open_label = label.new(CCVMonthlyShowDev ? timenow : na, m_open, xloc=xloc.bar_time, text=f_poc_label('mOpen', m_open), color=color.blue, textcolor=ShowLabelBackground ? CCVMonthlyTextColor : CCVMonthlyColor, style=ShowLabelBackgroundOption, size=size.small)
m_poc_label = label.new(CCVMonthlyShowDev ? timenow : na, m_poc, xloc=xloc.bar_time, text=f_poc_label('mPOC', m_poc), color=CCVMonthlyColor, textcolor=ShowLabelBackground ? CCVMonthlyTextColor : CCVMonthlyColor, style=ShowLabelBackgroundOption, size=size.small)
pm_poc_label = label.new(CCVMonthlyShowPrev ? timenow : na, pm_poc, xloc=xloc.bar_time, text=f_poc_label('pmPOC', pm_poc), color=CCVMonthlyColor, textcolor=ShowLabelBackground ? CCVMonthlyTextColor : CCVMonthlyColor, style=ShowLabelBackgroundOption, size=size.small)
pm_vah_label = label.new(CCVMonthlyShowPrev ? timenow : na, pm_vah, xloc=xloc.bar_time, text=f_poc_label('pmVAH', pm_vah), color=CCVMonthlyColor, textcolor=ShowLabelBackground ? CCVMonthlyTextColor : CCVMonthlyColor, style=ShowLabelBackgroundOption, size=size.small)
pm_val_label = label.new(CCVMonthlyShowPrev ? timenow : na, pm_val, xloc=xloc.bar_time, text=f_poc_label('pmVAL', pm_val), color=CCVMonthlyColor, textcolor=ShowLabelBackground ? CCVMonthlyTextColor : CCVMonthlyColor, style=ShowLabelBackgroundOption, size=size.small)

label.delete(m_open_label[1])
label.delete(m_poc_label[1])
label.delete(pm_poc_label[1])
label.delete(pm_vah_label[1])
label.delete(pm_val_label[1])
