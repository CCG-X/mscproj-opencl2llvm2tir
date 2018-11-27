; ModuleID = 'llvm_tmp.opt1.ll'
target datalayout = "e-m:o-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-apple-macosx10.14.0"

; Function Attrs: nounwind ssp uwtable
define void @write_pipe(i8 signext %ch00, i32* %data0) #0 {
  ret void
}

; Function Attrs: nounwind ssp uwtable
define void @read_pipe(i8 signext %ch00, i32* %dataInt0) #0 {
  ret void
}

; Function Attrs: nounwind ssp uwtable
define i32 @get_pipe_num_packets(i32 %a) #0 {
  ret i32 %a
}

; Function Attrs: nounwind ssp uwtable
define void @kernelInput(i32* noalias %aIn0, i32* noalias %aIn1, i32 %ch00, i32 %ch01) #0 {
  %data0 = alloca i32, align 4
  %data1 = alloca i32, align 4
  br label %1

; <label>:1                                       ; preds = %12, %0
  %i.0 = phi i32 [ 0, %0 ], [ %13, %12 ]
  %2 = icmp slt i32 %i.0, 10
  br i1 %2, label %3, label %14

; <label>:3                                       ; preds = %1
  %4 = sext i32 %i.0 to i64
  %5 = getelementptr inbounds i32, i32* %aIn0, i64 %4
  %6 = load i32, i32* %5, align 4
  store i32 %6, i32* %data0, align 4
  %7 = sext i32 %i.0 to i64
  %8 = getelementptr inbounds i32, i32* %aIn1, i64 %7
  %9 = load i32, i32* %8, align 4
  store i32 %9, i32* %data1, align 4
  %10 = trunc i32 %ch00 to i8
  call void @write_pipe(i8 signext %10, i32* %data0)
  %11 = trunc i32 %ch01 to i8
  call void @write_pipe(i8 signext %11, i32* %data1)
  br label %12

; <label>:12                                      ; preds = %3
  %13 = add nsw i32 %i.0, 1
  br label %1

; <label>:14                                      ; preds = %1
  ret void
}

; Function Attrs: nounwind ssp uwtable
define void @kernelCompute(i32 %ch00, i32 %ch01, i32 %ch1) #0 {
  %dataIn0 = alloca i32, align 4
  %dataIn1 = alloca i32, align 4
  %dataOut = alloca i32, align 4
  br label %1

; <label>:1                                       ; preds = %10, %0
  %i.0 = phi i32 [ 0, %0 ], [ %11, %10 ]
  %2 = icmp slt i32 %i.0, 10
  br i1 %2, label %3, label %12

; <label>:3                                       ; preds = %1
  %4 = trunc i32 %ch00 to i8
  call void @read_pipe(i8 signext %4, i32* %dataIn0)
  %5 = trunc i32 %ch01 to i8
  call void @read_pipe(i8 signext %5, i32* %dataIn1)
  %6 = load i32, i32* %dataIn0, align 4
  %7 = load i32, i32* %dataIn1, align 4
  %8 = add nsw i32 %6, %7
  store i32 %8, i32* %dataOut, align 4
  %9 = trunc i32 %ch1 to i8
  call void @write_pipe(i8 signext %9, i32* %dataOut)
  br label %10

; <label>:10                                      ; preds = %3
  %11 = add nsw i32 %i.0, 1
  br label %1

; <label>:12                                      ; preds = %1
  ret void
}

; Function Attrs: nounwind ssp uwtable
define void @kernelOutput(i32* noalias %aOut, i32 %ch1) #0 {
  %data = alloca i32, align 4
  br label %1

; <label>:1                                       ; preds = %13, %0
  %i.0 = phi i32 [ 0, %0 ], [ %14, %13 ]
  %2 = icmp slt i32 %i.0, 10
  br i1 %2, label %3, label %15

; <label>:3                                       ; preds = %1
  br label %4

; <label>:4                                       ; preds = %7, %3
  %5 = call i32 @get_pipe_num_packets(i32 %ch1)
  %6 = icmp eq i32 %5, 0
  br i1 %6, label %7, label %8

; <label>:7                                       ; preds = %4
  br label %4

; <label>:8                                       ; preds = %4
  %9 = trunc i32 %ch1 to i8
  call void @read_pipe(i8 signext %9, i32* %data)
  %10 = load i32, i32* %data, align 4
  %11 = sext i32 %i.0 to i64
  %12 = getelementptr inbounds i32, i32* %aOut, i64 %11
  store i32 %10, i32* %12, align 4
  br label %13

; <label>:13                                      ; preds = %8
  %14 = add nsw i32 %i.0, 1
  br label %1

; <label>:15                                      ; preds = %1
  ret void
}

attributes #0 = { nounwind ssp uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="core2" "target-features"="+cx16,+fxsr,+mmx,+sse,+sse2,+sse3,+ssse3" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"PIC Level", i32 2}
!1 = !{!"clang version 3.8.0 (tags/RELEASE_380/final)"}
