import React from "react";
import { Doughnut } from "react-chartjs-2";
import Chart from 'chart.js/auto';

function WeekDaysChart({props}) {
    const data = {
        labels: ['Автореги', 'БМ', 'ФП', 'Фарм', 'ПЗРД', 'Остальное'],
        datasets: [
            {
                label: 'Сумма ₽',
                data: [props.Autoreg_cost, props.BM_cost, props.FP_cost, props.Farm_cost, props.ZRD_cost, props.Undef_cost+props.PZRDFP_cost],
                backgroundColor: [
                    '#e86764',
                    '#f09620',
                    '#e5e979',
                    '#62e859',
                    '#67e1e8',
                    '#8b92ea',
                ],
                borderColor: '#ffffff',
                borderWidth: 3,
            },
            {
                label: 'Количество',
                data: [props.Autoreg_count, props.BM_count, props.FP_count, props.Farm_count, props.ZRD_count, props.Undef_count+props.PZRDFP_count],
                backgroundColor: [
                    'rgba(232,103,100, .5)',
                    'rgba(240,150,32, .5)',
                    'rgba(229,233,121, .5)',
                    'rgba(98,232,89, .5)',
                    'rgba(103,225,232, .5)',
                    'rgba(139,146,234, .5)',
                ],
                borderColor: '#ffffff',
                borderWidth: 3,
            },
        ]
    }
    
    const options = {
        responsive: true,
    }
    return (
        <div className="chart-container">
            <Doughnut data={data} options={options} />
        </div>
    );
}
export default WeekDaysChart;

