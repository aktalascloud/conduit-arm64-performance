// Only the source-built ONNX AAR from the verified recipe may satisfy this module.
allprojects {
    repositories {
        exclusiveContent {
            forRepository {
                maven { url = uri(rootProject.projectDir.resolve("../.avx1-work/native/maven")) }
            }
            filter { includeModule("com.microsoft.onnxruntime", "onnxruntime-android") }
        }
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

val newBuildDir: Directory = rootProject.layout.buildDirectory.dir("../../build").get()
rootProject.layout.buildDirectory.value(newBuildDir)

subprojects {
    val newSubprojectBuildDir: Directory = newBuildDir.dir(project.name)
    project.layout.buildDirectory.value(newSubprojectBuildDir)
}
subprojects {
    configurations.configureEach {
        resolutionStrategy.eachDependency {
            if (requested.group == "androidx.glance" && requested.name == "glance-appwidget") {
                useVersion("1.1.1")
                because("home_widget 0.9.1 declares glance-appwidget:1.+, which can resolve to alpha versions requiring newer Android tooling.")
            }
        }
    }
}
subprojects {
    project.evaluationDependsOn(":app")
}

tasks.register<Delete>("clean") {
    delete(rootProject.layout.buildDirectory)
}
