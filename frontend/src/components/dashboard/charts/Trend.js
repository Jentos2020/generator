import React from "react";
import { Bar } from "react-chartjs-2";
import Chart from 'chart.js/auto';


function TrendChart({ props }) {
  
    props = props.reverse();
    const data = {
        labels: props.map(prop => prop.day),
        datasets: [
            {
                label: 'Автореги',
                data: props.map(prop => prop.Autoreg_cost),
                backgroundColor: '#e86764',
                borderColor: '#ffffff',
                borderWidth: 1,
            },
            {
                label: 'БМ',
                data: props.map(prop => prop.BM_cost),
                backgroundColor: '#f09620',
                borderColor: '#ffffff',
                borderWidth: 1,
            },
            {
                label: 'ФП',
                data: props.map(prop => prop.FP_cost),
                backgroundColor: '#e5e979',
                borderColor: '#ffffff',
                borderWidth: 1,
            },
            {
                label: 'Фарм',
                data: props.map(prop => prop.Farm_cost),
                backgroundColor: '#62e859',
                borderColor: '#ffffff',
                borderWidth: 1,
            },
            {
                label: 'ПЗРД ФП',
                data: props.map(prop => prop.PZRDFP_cost),
                backgroundColor: '#67e1e8',
                borderColor: '#ffffff',
                borderWidth: 1,
            },
            {
                label: 'Остальное',
                data: props.map(prop => prop.Undef_cost),
                backgroundColor: '#8b92ea',
                borderColor: '#ffffff',
                borderWidth: 1,
            },
        ]
    }

    const options = {
        scales: {
            x: {
                stacked: true
            },
            y: {
                stacked: true,
                mirror: true,
            }
        },
        animations: false,
        barPercentage: 1,
    }


    return (
        <div className="chart-container">
            <Bar data={data} options={options} />
        </div>
    );
}
export default TrendChart;

