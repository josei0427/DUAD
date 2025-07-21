const student = {
	name: "John Doe",
	grades: [
		{name: "math",grade: 80},
		{name: "science",grade: 100},
		{name: "history",grade: 60},
		{name: "PE",grade: 90},
		{name: "music",grade: 98}
	]
}

let gradeAvg = 0;
let highestGrade = 0;
let lowestGrade = Infinity;
let highestSubject = "";
let lowestSubject = "";

for (i = 0; i < student.grades.length; i++){
    gradeAvg += student.grades[i].grade;

    if (i === student.grades.length - 1) {
        gradeAvg = gradeAvg / student.grades.length;
    }
}

for (i = 0; i < student.grades.length; i++){
    if (student.grades[i].grade > highestGrade){
        highestGrade = student.grades[i].grade;
        highestSubject = student.grades[i].name;
    }
}

for (i = 0; i < student.grades.length; i++){
    if (student.grades[i].grade < lowestGrade){
        lowestGrade = student.grades[i].grade;
        lowestSubject = student.grades[i].name
    }
}

const valueStudent = {
    name: student.name,
    gradeAvg: gradeAvg,
    highestGrade: highestSubject,
    lowestGrade: lowestSubject,
}

console.log(valueStudent)